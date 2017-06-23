from django.shortcuts import render
from django.db.models import Count
from .models import ProductDjangoItem, ProductReviewDjangoItem

import logging
logger = logging.getLogger(__name__)


def index(request):
    """View list of products"""
    logger.info('Requested index.')

    list_of_products = ProductDjangoItem.objects.all().annotate(numberOfReviews=Count('productreviewdjangoitem'))

    # Add other elements to each product item
    for p in list_of_products:

        # Remote thumbnail
        p.productThumbnailUrl = p.productImageUrl.replace('big', 'classic')

    context = dict()
    context['list_of_products'] = list_of_products

    return render(request, 'browser/index.html', context)


def product_view(request, productId):
    """View all reviews for a given product"""
    logger.info('Requested product view for product {0}.'.format(productId))

    this_product = ProductDjangoItem.objects.get(productId=productId)

    list_of_reviews = ProductReviewDjangoItem.objects.filter(
        productId=productId).order_by('-datePublished')
    context = dict()
    context['this_product'] = this_product
    context['list_of_reviews'] = list_of_reviews
    context['number_of_reviews'] = len(list_of_reviews)

    return render(request, 'browser/show_reviews.html', context)
