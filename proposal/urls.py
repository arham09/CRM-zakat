from django.urls import include, path

from .views import model_form_upload

app_name = 'proposal'

urlpatterns = [
    path('input/', model_form_upload , name='input'),

]