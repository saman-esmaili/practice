import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        self.url = url

    def permission_parse(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            content = self.response.text
            self.parsing = BeautifulSoup(content, "html.parser")
        else:
            raise Exception("This website didn't give you permission")


    def find_paragraphs(self):
        paragraphs = self.parsing.find_all("p")
        divs = self.parsing.find_all("div")
        file = open("paragraphs.csv","w",encoding="utf8")
        for paragraph in paragraphs:
            file.write(paragraph.text)
        for div in divs:
            file.write(div.text)
        file.close()

    def find_add_titles(self):
        title1 = self.parsing.find_all("h1")
        title2 = self.parsing.find_all("h2")
        title3 = self.parsing.find_all("h3")
        file = open("titles.csv","w",encoding="utf8")
        for h1 in title1:
            file.write(f"{h1.text},")
        for h2 in title2:
            file.write(f"{h2.text},")
        for h3 in title3:
            file.write(f"{h3.text},")
        file.close()

    def finder(self):
        self.permission_parse()
        self.find_add_titles()
        self.find_paragraphs()


url = input("enter website url:")
scarper = Scraper(url)
scarper.finder()
