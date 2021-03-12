from django.urls import path
from .views import SupplementDetail, SupplementCreate, SupplementUpdate, supplement_import, supplement_list, ShopDetail

urlpatterns = [
    path('supplement/', supplement_list, name='supplement_list'),
    path('supplement/c', SupplementCreate.as_view(), name='supplement_create'),
    path('supplement/u/<slug:slug>', SupplementUpdate.as_view(), name='supplement_update'),
    path('supplement/d/<slug:slug>', SupplementDetail.as_view(), name='supplement_detail'),
    path('supplement/import', supplement_import, name='supplement_import'),
    path('shop/d/<int:pk>', ShopDetail.as_view(), name='shop_detail'),
]