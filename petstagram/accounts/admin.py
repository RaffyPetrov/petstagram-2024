from django.contrib import admin

from petstagram.accounts.models import Profile


# Register your models here.


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin, )
    list_display = ('first_name', 'last_name')
