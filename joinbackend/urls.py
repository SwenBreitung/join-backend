"""
URL configuration for joinbackend project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from tasks.views import TaskViewSet
from todo.views import TodoViewSet
from contacts.views import ContactsViewSet
from accounts.views import LoginView, UserRegistrationView


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
 
]

