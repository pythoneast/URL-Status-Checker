from django.urls import path
from applications.urls import views

app_name = 'urls'

urlpatterns = [
    path('', views.url_list_view, name='url-list'),
    path('check/', views.check_url_status_view, name='check-url'),
]
