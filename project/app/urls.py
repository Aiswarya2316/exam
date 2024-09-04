from django.urls import path
from . import views
urlpatterns = [
    path('',views.addcntct),
    path('viewcntct',views.viewcntct),
    path('single/<int:id>',views.single),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),


]