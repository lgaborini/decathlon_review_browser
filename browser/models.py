from django.db import models


class ProductInQueue(models.Model):
    productUrl = models.URLField()


class ProductDjangoItem(models.Model):
    productId = models.CharField(max_length=100, primary_key=True)
    productName = models.CharField(max_length=100)
    last_fetched = models.DateTimeField()
    productUrl = models.URLField()
    productPrice = models.DecimalField(max_digits=5, decimal_places=2)
    productImageUrl = models.URLField()

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = "ProductDjangoItem"


class ProductReviewDjangoItem(models.Model):
    reviewHash = models.CharField(max_length=32, primary_key=True)
    productId = models.ForeignKey(ProductDjangoItem, on_delete=models.CASCADE)
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
    fit = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "ProductReviewDjangoItem"
