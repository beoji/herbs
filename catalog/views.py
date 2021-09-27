from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import DetailView, FormView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Supplement, Shop, Visitor
from .forms import SupplementImportForm, SupplementForm

import csv
import io


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def supplement_list(request):
    c = {}
    ip = get_client_ip(request)
    v = Visitor.objects.create(ip=ip)
    c['supplements'] = Supplement.objects.all()
    if request.user.is_authenticated:
        if request.method == 'GET':
            if request.GET.get('q'):
                order = request.GET.get('q')
                if order == 'daily_cost_min':
                    c['supplements'] = sorted(Supplement.objects.all(), key=lambda t: t.daily_cost_min)
                elif order == 'daily_cost_max':
                    c['supplements'] = sorted(Supplement.objects.all(), key=lambda t: t.daily_cost_max)
                else:
                    c['supplements'] = Supplement.objects.order_by(f'-{order}', 'name')
            if request.GET.get('search'):
                search_string = request.GET.get('search')
                c['supplements'] = Supplement.objects.filter(name__icontains=search_string)
            return render(request, 'catalog/supplement_list_form.html', c)
        if request.method == 'POST':
            pks = list(request.POST.keys())[1:]
            pks = list(map(int, pks))
            supplements = Supplement.objects.filter(pk__in=pks)
            user = request.user
            for supplement in supplements:
                supplement.users.add(user)
                supplement.save()
            for supplement in Supplement.objects.all():
                if supplement not in supplements:
                    supplement.users.remove(user)
            cost_min = sum(s.daily_cost_min for s in supplements)
            cost_max = sum(s.daily_cost_max for s in supplements)
            item_cost = sum(s.item_price for s in supplements)
            request.session['daily_cost_min_sum'] = str(cost_min)
            request.session['daily_cost_max_sum'] = str(cost_max)
            request.session['monthly_cost_min_sum'] = str(cost_min*31)
            request.session['monthly_cost_max_sum'] = str(cost_max*31)
            request.session['item_cost'] = str(item_cost)
            return render(request, 'catalog/supplement_list_form.html', c)
    return render(request, 'catalog/supplement_list.html', c)


class SupplementDetail(DetailView):
    model = Supplement
    context_object_name = 'supplement'


class SupplementCreate(UserPassesTestMixin, CreateView):
    form_class = SupplementForm
    template_name = 'catalog/supplement_create.html'

    def test_func(self):
        return self.request.user.is_staff


class SupplementUpdate(UserPassesTestMixin, UpdateView):
    model = Supplement
    form_class = SupplementForm
    template_name = 'catalog/supplement_create.html'

    def test_func(self):
        return self.request.user.is_staff


class ShopDetail(DetailView):
    model = Shop
    context_object_name = 'shop'


def supplement_import(request):
    if request.method == 'POST':
        form = SupplementImportForm(request.POST, request.FILES)
        if form.is_valid():
            decoded_file = form.cleaned_data['file'].read().decode('utf-8')
            file = io.StringIO(decoded_file)
            imported = list()
            rejected = list()
            for row in csv.DictReader(file, delimiter=','):
                try:
                    obj = Supplement(**row)
                    obj.save()
                    imported.append(obj)
                except:
                    rejected.append(row)
                    
            return render(request, 'catalog/supplement_import.html', {'imported': imported, 'rejected': rejected})
    else:
        form = SupplementImportForm()
    return render(request, 'catalog/supplement_import.html', {'form': form})


@login_required
def account_profile(request):
    user = request.user
    user_supplements = Supplement.objects.filter(users=user).order_by('category')
    return render(request, 'registration/account_profile.html', {'user_supplements': user_supplements})
