from django.contrib import admin
from .models import comment
# Register your models here.
@admin.register(comment)
class commentadmin(admin.ModelAdmin):
    list_display = ('text', 'comment_time')