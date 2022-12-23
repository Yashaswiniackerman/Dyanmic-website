from django.contrib import admin
from django.urls import path, include



from .views import index


# Django admin header customization

admin.site.site_header = "Techfnatic"
admin.site.site_title = "TechFnatic"
admin.site.index_title = "Welcome to TechFnatic"
urlpatterns = [
    path("index", index, name="index" )
] 


