# Register your models here. This will appear on the admin portion of the site
from django.contrib import admin

from .models import Question

admin.site.register(Question)