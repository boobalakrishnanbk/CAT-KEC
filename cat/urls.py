"""cat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from cat_app import views

urlpatterns = [
    path('admin/', admin.site.urls,),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('staff/', views.staff, name="staff"),

    path('', views.home, name='home'),

    path('student/', views.studentLogin, name='student_login'),

    path('result/', views.fetch_marks, name='fetch_marks'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
