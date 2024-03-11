# # necessary modules
# from django.urls import path
# from .views import Home
# from django.conf import settings
# from django.conf.urls.static import static
# # Define urlpatterns for the app
# urlpatterns = [
#     path('',Home.as_view(),name="home"),
#
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Import necessary modules
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView


# Define urlpatterns for the app
urlpatterns = [
    # Define a path for the home page
    path('', HomeView.as_view(), name="home"),
]

# If MEDIA_URL is specified in settings, serve media files
if hasattr(settings, 'MEDIA_URL') and hasattr(settings, 'MEDIA_ROOT'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
