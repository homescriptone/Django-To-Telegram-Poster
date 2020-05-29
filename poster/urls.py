from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, post_link

urlpatterns = [
   path('',index),
   path('post-link/', post_link)
]