from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),


    
    path('std',views.std,name='std'),
    path('show',views.show,name='show'),
    
    path('login',views.delete,name='delete'),
    path('delete<int:id>',views.delete,name='delete'),
    path('update<int:id>',views.update,name='update'), 
]
