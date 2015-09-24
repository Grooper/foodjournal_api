from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from foodjournal_api.core.views.food import FoodViewSet
from foodjournal_api.core.views.item import ItemViewSet


# Django REST Framework API routing
router = DefaultRouter()

# API Endpoints
router.register(r'foods', FoodViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = patterns(
	'',

	# API registration
	url(r'^api/', include(router.urls)),

    url(r'^api-admin/', include(admin.site.urls)),
)
