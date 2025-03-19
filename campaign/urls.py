from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateCheckoutSessionView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('projects/', views.projects, name='projects'),
    path('create-project/', views.create_project, name='create_project'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
    path('payment/', views.payment, name='payment'),
    path('payment_crypto/', views.payment_crypto, name='payment_crypto'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('admin/', admin.site.urls),
    path('payments/create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
