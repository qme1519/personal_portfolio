from django.contrib import admin
from user_interface.models import Type, Unit, BaseUnit, UpdateCurrency

# register all the models to be visible in the admin panel
class TypeAdmin(admin.ModelAdmin):
    pass

class UnitAdmin(admin.ModelAdmin):
    pass

class BaseUnitAdmin(admin.ModelAdmin):
    pass

class UpdateCurrencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, TypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(BaseUnit, BaseUnitAdmin)
admin.site.register(UpdateCurrency, UpdateCurrencyAdmin)
