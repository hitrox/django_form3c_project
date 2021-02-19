from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', views.start,name='form-start'),
    path('home/',views.home,name='form-home'),
    path('AboutUs/',views.aboutus,name='form-about'),
    path('Disclaimer/',views.disclaimer,name='form-disclaimer'),
    path('Feedback/',views.feedback,name='form-feedback'),
    path('profile/',views.profile,name='profile'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)