from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.user_register, name='reg'),
    path('home/<user>', views.home_page, name='home'),
    path('upload/', views.upload, name='upload'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('edit_user/<int:id>', views.edit_user, name='edit_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('logout/', views.LogoutPage, name='logout'),
    path('search_user', views.search_user, name='search_user'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
