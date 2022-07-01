from django.urls import path

from . import views

urlpatterns=[
    path('',views.api_overview,name='api_overview'),
    path('book-list/',views.booklist),
    path('add-book/',views.addbook),
    path('detail/<int:pk>/',views.viewbook,name='detail'),
    path('update/<int:pk>/',views.update,name='update'),
    path('deletebook/<int:pk>/',views.deletebook)

]