from django.contrib import admin

# Register your models here.

from .models import ProductInQueue
from .models import ProductDjangoItem
from .models import ProductReviewDjangoItem

admin.site.register(ProductInQueue)
admin.site.register(ProductDjangoItem)
admin.site.register(ProductReviewDjangoItem)
