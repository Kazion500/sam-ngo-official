from django.urls import path,include

from sam.views import home,log_out,log_in

urlpatterns = [
    path('',home,name="home"),
    path('logout/',log_out,name="logout"),
    path('login/',log_in,name="log_in")
]
