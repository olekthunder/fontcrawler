from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'bio', 'birth_date')

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)
