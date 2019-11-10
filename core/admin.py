from django.contrib import admin
from core.models import Primer

# Register your models here.

@admin.register(Primer)
class GeneAdmin(admin.ModelAdmin):
    list_display = ('id', 'fp', 'rp', 'submitter')