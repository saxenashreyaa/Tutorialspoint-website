from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries, AddTutorial 

from django.db import models
# Register your models here.






admin.site.register(Tutorial)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(AddTutorial)


