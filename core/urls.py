from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index, contact, signup, contact_dealer
from .forms import loginForm
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('contact-dealer/', contact_dealer, name='contact_dealer'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=loginForm), name='login'),
    path('admin/', admin.site.urls),
]
