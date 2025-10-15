import requests

class CollectGender:
    def __init__(self):
        self.data = ""


    def collect_gender(self, name):
        response = requests.get(url=f"https://api.genderize.io/?name={name}")
        self.data = response.json()
        return self.data

    def collect_age(self, name):
        response = requests.get(url=f"https://api.agify.io?name={name}")
        self.data = response.json()
        return self.data


response = requests.get(url="https://api.npoint.io/51e4bf5f576774206625")
data = response.json()

print(data)