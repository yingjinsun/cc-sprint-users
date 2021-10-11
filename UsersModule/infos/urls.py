from django.urls import path

from . import views

urlpatterns = {
    # ex: /infos/
    path('', views.index, name='index'),

    # ex: /infos/users
    path('users', views.users, name='users'),


    # ex: /infos/users/1
    path('users/<int:user_id>', views.getCertainUser, name='getUserByUserId'),
    # ex: /infos/users/1/address
    # path('<int:question_id>/results/', views.results, name='results'),

    # ex: /infos/addresses
    path('addresses', views.getAllAddresses, name='getAllAddresses'),
    # ex: /infos/addresses/1
    path('addresses/<int:address_id>', views.getCertainAddress, name='getAddressByAddressId'),
}