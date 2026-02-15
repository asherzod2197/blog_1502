from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('single/<int:id>/', single, name='single'),
    path('post/<int:id>/', post_comment, name='post_comment'),
]