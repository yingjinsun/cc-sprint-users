from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = {
    # ex: /infos/
    path('', views.index, name='index'),

    # ex: /infos/users
    re_path(r'^orders', views.users, name='usersWithField'),
    path('users', views.users, name='users'),

    # ex: /infos/users/1
    path('users/<int:user_id>', views.certainUser, name='getUserByUserId'),
    # ex: /infos/users/1/address
    # path('<int:question_id>/results/', views.results, name='results'),

    # ex: /infos/addresses
    path('addresses', views.addresses, name='addresses'),
    # ex: /infos/addresses/1
    path('addresses/<int:address_id>', views.certainAddress, name='getAddressByAddressId'),
}