"""finalrpoj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from researchers import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Registertion,name='register'),
    path('',views.getReasearch, name = 'home'),
    path('login/',views.Login,name = 'login'),
    path('logout/',views.Logout,name='logout'),
    path('add-Research/',views.addResearch,name='add-Research'),
    path('Find-Researchers/',views.GetResearchers,name = 'Find-Researchers'),
    path('details/<int:pk>',views.details,name='details'),
    path('rate/<int:pk>',views.rate,name='rate'),
    path('contact/',views.sendContact,name = 'contact'),
    path('details-research/<int:pk>',views.detailsResearch,name = 'details-research'),
    path('profile/<int:pk>',views.profile_details,name = 'profile-details'),
]

from rest_framework import routers
from researchers import  views as api_view
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('Research',api_view.aboutResearchViewSet)
router.register('users',api_view.userViewSet)
router.register('profile',api_view.profileViewSet)

urlpatterns += [
    path('api/',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/referesh',TokenRefreshView.as_view(),name='token_refresh'),
]

