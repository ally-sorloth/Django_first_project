from django.urls import path
from .views import home_view
from .views import home_about


urlpatterns = [
    path("home/", home_view),
    path("about/", home_about)
]
 