from django.contrib import admin

# Register your models here.
from news.models import News
from news.models import Section
from news.models import Source
from news.models import Image
admin.site.register(News)
admin.site.register(Section)
admin.site.register(Source)
admin.site.register(Image)

