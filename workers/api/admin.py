"""
This mod contains main settings about admin configuration
"""

from django.contrib import admin

from .models import Worker


admin.site.register(Worker)
