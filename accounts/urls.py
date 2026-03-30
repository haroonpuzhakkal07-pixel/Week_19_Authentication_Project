from django.urls import path
from .views import register_view, home_view, login_view, logout_view, admin_only_view, special_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view , name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-only/', admin_only_view, name='admin_only'),
    path('special/', special_view, name='special')
]