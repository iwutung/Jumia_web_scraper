# Jumia_web_scraper
This is a simple webscraping tool created with python Beautifulsoup.
This version is specific to jumia.ug, however with a few tweaks, it can
be applied to any location.

Data is colleted on the most popular products in the main categories:
'groceries', 'phones-tablets', 'home-office', 'electronics', 'health-beauty',
'category-fashion-by-jumia', 'computing', 'sporting-goods', 'baby-products',
'video-games', 'patio-lawn-garden', 'pet-supplies', 'toys-games', 'mlp-global-stores',
'miscellaneous', 'automobile', 'musical-instruments', 'books-movies-music', 
'services', 'industrial-scientific', 'wholesale'

Features extracted include:
date, shop, shop_score, product_category, brand_name, product_name, product_image, product_details, rating, v_rating, price, shipping_cost, free_delivery, reviews, product_url

Preliminary data cleaning is done and the result is exported as csv in the current working directory as "test_file_"+date_today+".csv"

This is work in progress, so any contributions are welcome.
