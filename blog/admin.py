from django.contrib import admin
from .models import *

class TableAdmin(admin.ModelAdmin):
    readonly_fields = ('pk', 'visits',)


admin.site.register(Info)
admin.site.register(Post, TableAdmin)
