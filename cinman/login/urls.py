from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login,name='login'),
    url(r'^success/',views.success,name='success'),
]
