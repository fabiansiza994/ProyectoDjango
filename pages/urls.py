from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:request_slug>', views.page, name="page")
]