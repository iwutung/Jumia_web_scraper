import pandas as pd
import numpy as np
import sys
import requests
from bs4 import BeautifulSoup
from datetime import date
import time
import random

# assign base Url
base_url = 'https://www.jumia.ug/'

# Overide user agent
UserAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)',
    'Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/6.1.6 Safari/537.78.2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.50.2 (KHTML, like Gecko) Version/5.0.6 Safari/533.22.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/6.2.8 Safari/537.85.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8',
    'MacOutlook/14.6.9.160926 (Intel Mac OS X 10.9.6)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10'
]

headers = {'User-Agent': random.choice(UserAgents)}

# create a list containing product links
product_links = []
categories = [
    'groceries', 'phones-tablets', 'home-office', 'electronics', 'health-beauty', 'category-fashion-by-jumia',
    'computing', 'sporting-goods', 'baby-products', 'video-games', 'patio-lawn-garden', 'pet-supplies', 'toys-games',
    'mlp-global-stores', 'miscellaneous', 'automobile', 'musical-instruments', 'books-movies-music', 'services',
    'industrial-scientific', 'wholesale'
]

start_time = time.time()


for category in categories:
    for page in range(1, 4):

        sub_url = f'https://www.jumia.ug/{category}/?viewType=list&page={page}#catalog-listing'

        response = requests.get(sub_url, headers=headers)

        # create a beautifulsoup object from the HTML response
        soup = BeautifulSoup(response.content, 'lxml')

        # assign product list
        product_list = soup.find_all('article', class_="prd _fl c-prd")

        print('Checking: ', sub_url)

        # add every link in the product list to product_links
        for item in product_list:
            for link in item.find_all('a', href=True):
                product_links.append(base_url + link['href'])

        print('adding: ', sub_url)

    # go to next link

print('number of products captured: ', len(product_links))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

start_time = time.time()
product_data = []

for link in product_links:
    trycnt = 5  # max try cnt
    while trycnt > 0:
        try:

            # assign test response
            link_response = requests.get(link, headers=headers)

            # create beautifulsoup
            soup = BeautifulSoup(link_response.content, 'lxml')

            # assign variables
            date = pd.to_datetime("today").date()

            try:
                shop = soup.find('p', class_="-m -pbs").text.strip()

            except AttributeError:
                pass

            try:
                product_name = soup.find('h1', class_="-fs20 -pts -pbxs").text.strip()

            except AttributeError:
                pass

            try:
                product_image = soup.find('img', class_="-fw -fh")['data-src']

            except:
                pass

            try:
                product_details = soup.find('div', class_="markup -mhm -pvl -oxa -sc").text.strip()

            except AttributeError:
                pass

            try:
                category = soup.find('a', class_="cbs").next_sibling.text.strip()

            except AttributeError:
                pass

            try:
                brand_name = soup.find(lambda tag: tag.name == 'a' and tag.get(
                    'class') == ['_more'], target=False).text.strip()

            except AttributeError:
                brand_name = 'Not Named'

            try:
                rating = soup.find('div', class_="stars _s _al").text.strip()

            except AttributeError:
                rating = np.nan

            try:
                v_rating = soup.find('p', class_="-fs16 -pts").text.strip()

            except AttributeError:
                v_rating = np.nan

            try:
                price = soup.find('span', dir="ltr", class_="-b -ltr -tal -fs24").text.strip()

            except AttributeError:
                pass

            try:
                shipping_cost = soup.find('em').text.strip()

            except AttributeError:
                pass

            try:
                reviews = soup.find('h2', class_="-fs14 -m -upp -ptm").text.strip()

            except AttributeError:
                reviews = np.nan

            try:
                shop_score = soup.find('bdo', class_="-m -prxs", dir="ltr").text.strip()

            except AttributeError:
                pass

            try:
                free_delivery = soup.find('p', class_=False).text.strip()

                if free_delivery != 'Eligible for Free Delivery.\xa0Details':
                    free_delivery = 'Not Eligible'

                else:
                    free_delivery

            except AttributeError:
                pass

            # Create the data dictionary
            products = {
                'date': date,
                'shop': shop,
                'shop_score': shop_score,
                'product_category': category,
                'brand_name': brand_name,
                'product_name': product_name,
                'product_image': product_image,
                'product_details': product_details,
                'rating': rating,
                'v_rating': v_rating,
                'price': price,
                'shipping_cost': shipping_cost,
                'free_delivery': free_delivery,
                'reviews': reviews,
                'product_url': link
            }

            product_data.append(products)

            print('Saving ', products['product_name'])

            trycnt = 0  # success

        except requests.exceptions.ConnectionError as ex:
            if trycnt <= 0:
                print("Failed to retrieve: " + link + "\n" + str(ex))  # done retrying
            else:
                trycnt -= 1  # retry

            time.sleep(1.5)  # wait 1/2 second then retry
      # go to next link

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

df = pd.DataFrame(product_data)
df.v_rating = df.v_rating.apply(lambda x: 'Not Available' if pd.isna(
    x) else x.split(' ')[0]).astype('int', errors='ignore')
df.rating = df.rating.apply(lambda x: 'Not Available' if pd.isna(
    x) else x.split(' ')[0]).astype('float', errors='ignore')
df.loc[df.v_rating == 'Not Available', 'rating'] = 'Not Available'
df.price = df.price.apply(lambda x: np.nan if pd.isna(x) else x.split(
    ' ')[1]).str.replace(',', '').astype('int', errors='ignore')
df.shipping_cost = df.shipping_cost.apply(lambda x: np.nan if pd.isna(x) else x.split(' ')[
                                          1]).str.replace(',', '').astype('int', errors='ignore')
df.reviews = df.reviews.apply(lambda x: x if pd.isna(x) else x.split(' ')[
                              2]).str.slice(1, -1).astype('int', errors='ignore')
df.loc[df.v_rating == 'Not Available', 'reviews'] = 'None Yet'
df.drop_duplicates(inplace=True)

# export DataFrame to csv
date_today = date.today().strftime("%d-%m-%Y")
file_name = "test_file_"+date_today+".csv"
df.to_csv(file_name, index=False)
