from django.urls import path, include
from . import views # Import views to connect routes to view functions
from .views import butterflyList
from django.contrib import admin

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/',views.about, name='about'),
  path('butterflies/', views.butterflies_index, name='butterflies-index'),
  path('butterflies/<int:butterflies_id>/', views.butterflies_detail, name='butterflies-detail'), 
  path('butterflies/create/', views.butterflyCreate.as_view(), name='butterfly_create'),
  path('butterflies/', butterflyList.as_view(), name='butterfly_index'),
  path('butterflies/<int:pk>/update/', views.butterfliesUpdate.as_view(), name='butterflies-update'),
  path('butterflies/<int:pk>/delete/', views.butterfliesDelete.as_view(), name='butterflies-delete'),
  path('butterflies/<int:butterflies_id>/add-feeding/',views.add_feeding,name='butterflies-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('butterflies/<int:butterfly_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
  path('butterflies/<int:butterflies_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),
  path('cats/<int:cat_id>/add-photo/', views.add_photo, name='add-photo'),
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  ]