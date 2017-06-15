# Decathlon review browser

Browse Decathlon reviews scraped using [lgaborini/decathlon_review_scraper](../../../../lgaborini/decathlon_review_scraper).

The project hosts a Django website to read all stored reviews.

At the moment, the scraping must be done manually.   
An extension to programmatically run Scrapy is planned.

The project defines also the [schema](browser/models.py) for `Items` obtained using Scrapy: 

# Usage:

## Tested under:
* Anaconda Python 4.2.13

## Requirements:
* Python 3.5.2
* Django
* scrapy-djangoitem

