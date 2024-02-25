"""
URL configuration for neosTicaret project.

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
from products.views import *
from user.views import *

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index ,name='index'),
    path('product/<int:productId>',detail,name='detail-page'), 
    # productId nereden geldi?
    path('user/register/',register,name='register'),
    path('user/login/',userLogin,name='login'),
    path('user/logout',userLogout,name="logout"),
    path('create/',create,name="create")
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
# burayı ve settingsteki medıa ayarlarını sadece ezberlesek olur mu bi mantığı var mı?
