from django.urls import include, path

from .import views

app_name = 'donatur'

urlpatterns = [
    path('', views.DonaturListView.as_view(), name='donatur_list'),
    path('daftar-donasi', views.DonasiListView.as_view(), name='donasi_list'),
    path('donatur/', views.DonaturCreateView.as_view(), name='donatur_add'),
    path('donation/', views.DonasiCreateView.as_view(), name='donasi_add'),
    #path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    #path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
