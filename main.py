import requests
class Wrapper():
    def __init__(self,url) -> None:
        self.url = url
    def get_all_items(self):
        url = f"{self.url}/items"
        resp = requests.get(url=url).json()
        return resp
wp = Wrapper("http://127.0.0.1:8000")
print(wp.get_all_items())