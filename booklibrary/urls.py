"""booklibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ebook import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', views.sign_up, name ='sign_up'),
    path('user_login/', views.user_login, name ='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('book_upload/', views.book_upload, name='book_upload'),
    path('', views.book_list, name='book_list'),
    path('delete/<int:id>', views.delete_book, name='delete_book'),
    path('user_profile/<str:username>', views.get_user_profile, name='user_profile'),
    path('search', views.search, name="search"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



