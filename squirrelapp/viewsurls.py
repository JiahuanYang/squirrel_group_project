from django.urls import path, re_path
  
from . import views

app_name = 'squirrelapp'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<slug:squirrel_id>/', views.update, name='update'),
    path('<slug:squirrel_id>/update/', views.update_lati, name='request'),
    path('add/',views.sightingsadd,name = 'add'),
    path('stats/',views.sightingsstats,name='stats'),
    # Need to find out how to direct to path /sightings/<unique-squirrel-id>
    # path('',views.sightingslist),
    ]
