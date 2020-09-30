from django.contrib import admin
from .models import counting

# Register your models here.
class countAdmin(admin.ModelAdmin):
    pass

admin.site.register(counting,countAdmin)

