from django.urls import path
from . import views
urlpatterns = [
    path('',  views.show),
    path('<int:article_id>', views.detail, name="detail"),
]