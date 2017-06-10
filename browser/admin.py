from django.contrib import admin

# Register your models here.

from .models import ProductInQueue
from .models import Product
from .models import ProductReview

admin.site.register(ProductInQueue)
admin.site.register(Product)
admin.site.register(ProductReview)