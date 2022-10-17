"""profiles_project URL Configuration

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

from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register("profile",views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("hello-view/",views.HelloApiView.as_view()),
    path("login/",views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
