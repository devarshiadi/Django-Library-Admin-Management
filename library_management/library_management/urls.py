from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from authentication.views import signup_view, login_view, logout_view
from books.views import student_book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/books/', include('books.urls')),
    
    # Frontend URLs
    path('', student_book_list, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('books/', include('books.urls_frontend')),
]