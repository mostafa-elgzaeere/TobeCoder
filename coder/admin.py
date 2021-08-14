from django.contrib import admin
from .models import Track,Curse,Video

# Register your models here.

class CurseInline(admin.TabularInline):
    model=Curse


class VideoInline(admin.TabularInline):
    model=Video



@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    inlines=[CurseInline]


@admin.register(Curse)
class CurseAdmin(admin.ModelAdmin):
    inlines=[VideoInline]


