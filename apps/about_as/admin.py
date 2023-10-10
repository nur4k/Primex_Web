from django.contrib import admin

from apps.about_as.models import About_As, FeedBack


admin.site.register((About_As, FeedBack))
