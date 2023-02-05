from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.show,name="show"),
    path('full/<int:id>/', views.full,name="full"),
    path('mylogin',views.login,name="mylogin"),
    path('comments',views.comments,name='comments'),
    path('mylogout',views.logout,name='mylogout'),
    path('reg',views.register,name='register'),
    path('enq',views.enquiry,name='enquiry'),
    path('srch',views.search,name='srch'),
    path('add',views.add,name="add"),
    path('del/<int:id>',views.de,name='del'),
    path('category/<int:id>',views.showbycat,name="category")
]
