from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
# from contact_us import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'', views.ContactusViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]














# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views
# router = DefaultRouter() # amader router

# router.register('', views.ContactusViewset) # router er antena
# urlpatterns = [
#     path('', include(router.urls)),
# ]