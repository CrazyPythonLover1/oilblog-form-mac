"""oilblog URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import (
    IndexView,
    PostDetailView,
    LikeView,
    # PostCategory,
    
    CanolaOilList,
    CoconutOilList,
    CornOilList,
    CottonseedOilList,
    OliveOilList,
    PalmOilList,
    PeanutOilList,
    RapeseedOilList,
    SunflowerOilList,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>/', LikeView ,name='like-post'),


    # cATEGORIES URL 
    # path('post/cat/<int:pk>/', PostCategory.as_view(), name='post-category'),

    path('CanolaOil', CanolaOilList.as_view(), name='CanolaOil'),
    path('CoconutOil', CoconutOilList.as_view(), name='CoconutOil'),
    path('CornOil', CornOilList.as_view(), name='CornOil'),
    path('CottonseedOil', CottonseedOilList.as_view(), name='CottonseedOil'),
    path('OliveOil', OliveOilList.as_view(), name='OliveOil'),
    path('PalmOil', PalmOilList.as_view(), name='PalmOil'),
    path('PeanutOil', PeanutOilList.as_view(), name='PeanutOil'),
    path('RapeseedOil', RapeseedOilList.as_view(), name='RapeseedOil'),
    path('SunflowerOil', SunflowerOilList.as_view(), name='SunflowerOil'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)


