from django.contrib import admin
from .models import *

# Register your models here.

class ToolPageTranslationInline(admin.StackedInline):
    model = ToolPageTranslation
    extra = 1

@admin.register(ToolPage)
class ToolPageAdmin(admin.ModelAdmin):
    inlines = [ToolPageTranslationInline]
    list_display = ('tool', 'custom_url')