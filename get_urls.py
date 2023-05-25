import requests
from bs4 import BeautifulSoup
import os

urls = ["https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPKWA3/t%C3%A0i-kho%E1%BA%A3n-c%E1%BB%A7a-t%C3%B4i",
       "https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPGWA3/%C4%91%E1%BA%B7t-h%C3%A0ng-v%C3%A0-thanh-to%C3%A1n",
       "https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPJWA3/giao-nh%E1%BA%ADn-h%C3%A0ng",
       "https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPIWA3/%C4%91%E1%BB%95i-tr%E1%BA%A3-b%E1%BA%A3o-h%C3%A0nh-v%C3%A0-b%E1%BB%93i-ho%C3%A0n",
       "https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPHWA3/d%E1%BB%8Bch-v%E1%BB%A5-v%C3%A0-ch%C6%B0%C6%A1ng-tr%C3%ACnh",
       "https://hotro.tiki.vn/s/topic/0TO5Y00000BiIPLWA3/th%C3%B4ng-tin-v%E1%BB%81-tiki"]

with open(f"{os.getcwd()}/ho_tro_urls.txt", "w") as f:
    # Send a GET request to the URL
    for url in urls:
        response = requests.get(url)
        # print(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all the <a> tags with class "t-articles-list__item-link"
            article_links = soup.find_all("a", class_="article-link selfServiceArticleHeaderDetail")

            # Extract the href attribute (link) from each <a> tag
            links = [link.get("href") for link in article_links]

            # Print the extracted links
            for link in links:
                f.writelines(link)
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
