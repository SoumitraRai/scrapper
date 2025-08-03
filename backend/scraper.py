import requests
from bs4 import BeautifulSoup
import redis
import json
import lxml

def scrape_page_elements(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # print(soup.prettify())  # For debugging purposes, to see the HTML structure
        # with open("scraped_cont.txt", "w") as file: #saves scraped content to a text file
            # file.write(soup.prettify())


        # TODO: Scrape the head element -> Done
        # Refer to BeautifulSoup documentation for more details on how to scrape elements.
        head = soup.find('head')

        # TODO: Scrape the header element. -> Done
        # Note: The header is a div with class 'bs-header' on the page we're using.
        header = soup.find('div', class_='bs-header')

        #Scraping the Product Cards. Since it was given in the readme and I am confused about it.
        product_cards = soup.find_all('div', class_='cp-product typ-plp plp-srp-typ')
        products = []
        for card in product_cards:
            title = card.find('h3', class_='product-title plp-prod-title 999') # type: ignore
            sale_price = card.find('span', class_='amount plp-srp-new-amount') # type: ignore
            original_price = card.find('span', class_='amount', id='old-price') # type: ignore
            discount_percentage = card.find('span', class_='discount discount-mob-plp discount-newsearch-plp') # type: ignore
            
            # Commented out as they were not working properly
            # discount_value = card.find('span', class_='discount-value') # type: ignore
            # rating = card.find('span', class_='rating-text') # type: ignore

            # review_count = card.find('span', style="color: rgb(255, 255, 255);") # type: ignore
            # offers_and_features = card.find('div', class_='tagsForPlp') # type: ignore
            # delivery = None
            # if (delivery_container := card.find('span', class_='delivery-text-msg')): # type: ignore
            #     delivery = (inner_span.text.strip() if (inner_span := delivery_container.find('span')) else delivery_container.get_text(strip=True)) # type: ignore

            ## Tried to scrape Images but was not able to do so. Hence commented out the code.
            # product_img = card.find('img') # type: ignore
            # link_img = None
            # if product_img is not None:
            #     if product_img.get('data-src'):
            #         link_img = product_img['data-src']
            #     elif product_img.get('src'):    
            #         link_img = product_img['src']
            #     else:
            #         link_img = 'https://placehold.co/400x400/png?text=No+Image'
            # else: link_img = 'https://placehold.co/400x400/png?text=No+Image'


            product_info = {
                "title": title.text.strip() if title else None,
                "sale_price": sale_price.text.strip() if sale_price else None,
                "price": original_price.text.strip() if original_price else None,
                "discount_percentage": discount_percentage.text.strip() if discount_percentage else None,
                # "discount_value": discount_value.text.strip() if discount_value else None,
                # "rating": rating.text.strip() if rating else None,
                # "review_count": review_count.text.strip() if review_count else None,
                # "offers_and_features": offers_and_features.text.strip() if offers_and_features else None,
                # "delivery": delivery,
                # "product_img": link_img if link_img else None,
            }
            # print("\n")  # For debugging purposes, to see the scraped product info
            # print(product_info)
            products.append(product_info)
        # if not products: # for checking wheter products were scraped or not
        #     print("Warning: No products found.")


        return {"head": str(head) if head else None, "header": str(header) if header else None, "products": products}

    except Exception as e:
        print(f"Error scraping page elements: {e}")
        return {"head": None, "header": None, "products": None}

def store_in_redis(data):
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set("scraped_content", json.dumps(data))
        print("Data stored in Redis") #added for debugging
    except Exception as e:
        print(f"Data not stored in Redis: {e}") #added for debugging



if __name__ == "__main__":
    url = "https://www.croma.com/televisions-accessories/c/997"
    page_elements = scrape_page_elements(url)
    store_in_redis(page_elements)
    print("Data scraped and stored.")