from .models import *


class DataMixin:

    def get_user_context(self, **kwargs):

        context = kwargs
        top = UserProfile.objects.order_by('-correct')[:5]
        context['top'] = top

        return  context