from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')  # Показать поля в списке
    search_fields = ('first_name', 'last_name', 'email')  # Поля для поиска
