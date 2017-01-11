from django.contrib import admin

# Register your models here.
from .models import News
from .models import Section
from .models import Source
admin.site.register(News)
admin.site.register(Section)
admin.site.register(Source)

