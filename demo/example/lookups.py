from django.core.exceptions import PermissionDenied
from ajax_select import register, LookupChannel
from .models import Product

@register('product')
class ProductLookup(LookupChannel):

    model = Product

    def get_query(self, q, request):
        print('ajax query', q, request)
        return self.model.objects.filter(name__icontains=q).order_by('name')

    def check_auth(self, request):
        # if not request.user.is_staff:
        #     raise PermissionDenied
        pass