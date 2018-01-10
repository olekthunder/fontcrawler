from django.contrib import admin
from .models import Font


class FontAdmin(admin.ModelAdmin):
    class Meta:
        model = Font


admin.site.register(Font, FontAdmin)