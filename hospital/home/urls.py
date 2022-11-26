from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name="about"),
    path('booking/',views.book,name="book"),
    path('doctors/',views.doct,name="doct"),
    path('department/',views.dep,name="dep"),
    path('contact/',views.cont,name="cont")

]
