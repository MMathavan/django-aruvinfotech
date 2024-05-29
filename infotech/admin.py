from django.contrib import admin
from .models import contact1

class contactAdmin(admin.ModelAdmin):
    # class Meta:
    #     model = contact1
    #     fields = '__all__'
    list_display = ('name','email','mobileno','message')
admin.site.register(contact1,contactAdmin)

# Register your models here.

# Register your models here.
