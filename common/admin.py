from django.contrib import admin
from .models import *
from nested_admin import NestedTabularInline, NestedModelAdmin


class SubHeaderInline(NestedTabularInline):
    model = SubHeader
    extra = 1

class TranslationHeaderInline(NestedTabularInline):
    model = TranslationHeader
    inlines = [SubHeaderInline]
    extra = 1


class HeaderAdmin(NestedModelAdmin):
    inlines = [TranslationHeaderInline]

admin.site.register(Header, HeaderAdmin)
admin.site.register(Url)


class SubFooterInline(NestedTabularInline):
    model = SubFooter
    extra = 1

class TranslationFooterInline(NestedTabularInline):
    model = TranslationFooter  # Corrected model name
    inlines = [SubFooterInline]
    extra = 1

class FooterAdmin(NestedModelAdmin):
    inlines = [TranslationFooterInline]

admin.site.register(Footer, FooterAdmin)
