from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# class InventoryFilter(admin.SimpleListFilter):
#     title = 'inventory'
#     parameter_name = 'inventory'

#     def lookups(self, request, model_admin):
#         return [
#             ('<10', 'Low')
#         ]

#     def queryset(self, request, queryset: QuerySet):
#         if self.value() == '<10':
#             return queryset.filter(inventory__lt=10)

@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['county']
    # list_editable = ['county']
    list_per_page = 10


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = ['username',
                     'gender', 'phone' ]

    def username(self, obj):
        return obj.user.username
    # ]
    # list_editable = [ 'age']
    # list_per_page = 10
    # # list_select_related = ['collection']
    # search_fields = ['first_name']

    # def patient_titl(self, product):
    #     return product.collection.title

    # @admin.display(ordering='inventory')
    # def inventory_status(self, product):
    #     if product.inventory < 10:
    #         return 'Low'
    #     return 'OK'

    # @admin.action(description='Clear inventory')
    # def clear_inventory(self, request, queryset):
    #     updated_count = queryset.update(inventory=0)
    #     self.message_user(
    #         request,
    #         f'{updated_count} products were successfully updated.',
    #         messages.ERROR
    #     )



@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'age']
    list_editable = ['age']
    list_per_page = 10
    def username(self, obj):
        return obj.user.username
    # ordering = ['first_name', 'last_name']
    # search_fields = ['first_name__istartswith', 'last_name__istartswith']

    # @admin.display(ordering='orders_count')
    # def orders(self, customer):
    #     url = (
    #         reverse('admin:store_order_changelist')
    #         + '?'
    #         + urlencode({
    #             'customer__id': str(customer.id)
    #         }))
    #     return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(
    #         orders_count=Count('order')
    #     )


