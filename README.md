# Decathlon review browser

Browse Decathlon reviews scraped using [lgaborini/decathlon_review_scraper](../../../../lgaborini/decathlon_review_scraper).

The project hosts a Django website to read all stored reviews.

At the moment, the scraping must be done manually.   
An extension to programmatically run Scrapy is planned.

The project defines also the [schema](browser/models.py) for `Items` obtained using Scrapy.

# Usage:   
See Django documentation on the first run of a Django site.

> python manage.py runserver   

Connect on `http://127.0.0.1:8000/`.

## Tested under:
* Anaconda Python 4.2.13

## Requirements:
* Python 3.5.2
* Django
* scrapy-djangoitem

## TODO:

- [x] Add product image display
- [x] Add product image thumbnails in review list
- [ ] Add Translate button next to reviews
- [ ] Add sort columns in review/product list
- [ ] Add product image in review list
- [ ] Launch the Scrapy scraper (using Celery?)
