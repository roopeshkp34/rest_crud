
from django.urls import path
from . import views
  
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name ='hello'),
    path('snipets_list/', views.SnippetsView.as_view(), name ='View'),
    path('snipets_details/<int:pk>', views.DetailView.as_view(), name ='Details'),
    path('tag_list', views.TagView.as_view(), name ='Tag View'),

    path('tag_details/<int:pk>', views.TagDetails.as_view(), name ='Tag Details'),


]