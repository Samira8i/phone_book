from django.urls import path
from .views import contact_list, add_contact, edit_contact, delete_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:contact_id>/', edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>/', delete_contact, name='delete_contact'),
]
