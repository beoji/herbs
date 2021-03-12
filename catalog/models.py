from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

# Properties
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Neurotransmitter(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Producent(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'pk': self.pk})


class Supplement(models.Model):
    name = models.CharField(max_length=50, unique=True)
    polish_name = models.CharField(max_length=50, blank=True, null=True)
    users = models.ManyToManyField(User, related_name = 'user', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    neurotransmitters = models.ManyToManyField(Neurotransmitter, blank=True)
    description = models.TextField(blank=True, null=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    item_weight = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    portion_weight_min = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    portion_weight_max = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    daily_intakes_min = models.IntegerField(blank=True, null=True)
    daily_intakes_max = models.IntegerField(blank=True, null=True)
    meal_relation = models.CharField(max_length=1, choices=(('B', 'Before meal'), ('W', 'With meal'), ('A', 'After meal')), blank=True, null=True)
    country_of_origin = models.CharField(max_length=50, blank=True, null=True)
    date_of_discovery = models.DateField(blank=True, null=True)
    bioavailability = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    producent = models.ForeignKey(Producent, blank=True, null=True, on_delete=models.SET_NULL)
    shop = models.ForeignKey(Shop, blank=True, null=True, on_delete=models.SET_NULL)
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=40, blank=True, unique=True)

    @property
    def daily_cost_min(self):
        a = self.item_price and self.item_weight and self.portion_weight_min and self.daily_intakes_min
        if a:
            unit_price = self.item_price / self.item_weight
            daily_cost = unit_price * self.portion_weight_min * self.daily_intakes_min
            return round(daily_cost, 2)
        else:
            return 0

    @property
    def daily_cost_max(self):
        a = self.item_price and self.item_weight and self.portion_weight_max and self.daily_intakes_max
        if a:
            unit_price = self.item_price / self.item_weight
            daily_cost = unit_price * self.portion_weight_max * self.daily_intakes_max
            return round(daily_cost, 2)
        else:
            return 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('supplement_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
