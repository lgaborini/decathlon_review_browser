from django.db import models


class ProductInQueue(models.Model):
    productUrl = models.URLField()


class Product(models.Model):
    productId = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    last_fetched = models.DateTimeField()
    productUrl = models.URLField()

    def __str__(self):
        return self.productName


class ProductReview(models.Model):
    productId = models.ForeignKey(Product)
    ratingValue = models.CharField(max_length=100)
    datePublished = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.CharField(max_length=10960)
    usedSince = models.CharField(max_length=100)
    reviewBonus = models.CharField(max_length=100)
    reviewMalus = models.CharField(max_length=100)
    reviewTitle = models.CharField(max_length=100)
    reviewReply = models.CharField(max_length=10960)
    fit = models.CharField(max_length=100)
