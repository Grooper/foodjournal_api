from rest_framework import viewsets

from foodjournal_api.core.models.item import Item
from foodjournal_api.core.serializers.item import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `Item` Model
	"""
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_fields = ()
