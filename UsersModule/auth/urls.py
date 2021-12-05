from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = {
    path('', views.index, name='index'),
    # path('<int:token>', views.index, name='index'),
    # path('addresses', views.addresses, name='addresses'),
    # path('addresses/<int:address_id>', views.certainAddress, name='getAddressByAddressId'),
}