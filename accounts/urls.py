from django.contrib import admin
from django.urls import path
from task import views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup, name='signup'),
    path('log_in',views.log_in, name='log_in'),
    path('logout',views.logout),
    # path('video',views.video),

]