import requests


class Wrapper:
    def __init__(self, url) -> None:
        self.url = url

    def get_all_items(self):
        lengthurl = f"{self.url}/itemslength"
        url = f"{self.url}/items"
        lenresponse = requests.get(lengthurl).json()
        length = int(lenresponse[0]["length"])
        resp = requests.get(url=url).json()
        items = []
        for i in range(0, length):
            items.append(resp[i])
        return items
    def getlength(self):
        lengthurl = f"{self.url}/itemslength"
        lenresponse = requests.get(lengthurl).json()
        length = int(lenresponse[0]["length"])
        return length


wp = Wrapper("http://127.0.0.1:8000")
length = wp.getlength()
items = wp.get_all_items()
for item in range(0,length):
    print(f"{items[item]["name"]}, {items[item]["price_in_euro"]}, {items[item]["typ"]}.")
