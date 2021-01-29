from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from regapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('login/registration.html', views.login, name='login'),



    path("login/about/", views.index, name="index"),
    path("login/about/contact/", views.contact, name="ContactUs"),
    path("login/about/tracker/", views.tracker, name="TrackingStatus"),
    path("login/about/search/", views.search, name="Search"),
    path("login/about/products/<int:myid>", views.productView, name="ProductView"),
    path("login/about/checkout/", views.checkout, name="Checkout")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




urlpatterns+=staticfiles_urlpatterns()