from django.shortcuts import render
from .models import ProductDjangoItem, ProductReviewDjangoItem

from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Requested index.')

    list_of_products = ProductDjangoItem.objects.all()
    context = dict()
    context['list_of_products'] = list_of_products

    return render(request, 'browser/index.html', context)


def product_view(request, productId):
    logger.info('Requested product view for product {0}.'.format(productId))

    this_product = ProductDjangoItem.objects.get(productId=productId)

    list_of_reviews = ProductReviewDjangoItem.objects.filter(productId=productId)
    context = dict()
    context['this_product'] = this_product
    context['list_of_reviews'] = list_of_reviews

    return render(request, 'browser/show_reviews.html', context)
    return HttpResponse('Requested product view for product {0}.'.format(productId))
