from django.contrib import admin
from django.urls import path
from task import views
from doubt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('next',views.next, name='next'),
    

]