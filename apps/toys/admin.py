from django.contrib import admin

from apps.toys.models import Toy

class Toys(admin.ModelAdmin):
    list_display = ('id','created','name','description','toy_category','release_date','was_include_in_home')
    list_display_links = ('id','name',)
    list_per_page=20
    search_fields = ('nome',)

admin.site.register(Toy,Toys)
