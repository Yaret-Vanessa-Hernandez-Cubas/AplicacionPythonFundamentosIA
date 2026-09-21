from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TipoIA, Concepto, Infografia


admin.site.register(TipoIA)
admin.site.register(Concepto)
admin.site.register(Infografia)