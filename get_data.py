import requests
import os
from bs4 import BeautifulSoup
c = 0
with open(f"{os.getcwd()}/ho_tro_urls.txt", "r") as f:
    url_list = f.readlines()
    for url in url_list:
        res = requests.get(url=str(url))
        soup = BeautifulSoup(res.content,  "html.parser")
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.body.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        filename = str(url).split("/")[-1]
        if not os.path.exists(f"{os.getcwd()}/clean"):
                os.makedirs(f"{os.getcwd()}/clean")
        out_file = os.path.join(f"{os.getcwd()}/clean", f"{filename}.txt")
        out = open(out_file, "w")
        out.write(text)
        out.close 