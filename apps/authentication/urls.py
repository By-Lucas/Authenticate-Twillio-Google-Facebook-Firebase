from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from verify_project import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('login/', views.auth_view, name='login-view'),
    path('verify/', views.verify_view, name='verify-view'),
    path('logout/', views.logount_view, name='logout')
]

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)