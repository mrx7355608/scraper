from bs4 import BeautifulSoup
import math 
import random
import json

names = []
desc = []
images = []

with open("./html-files/vegetablejuice.hbs") as file:
    soup = BeautifulSoup(file, "html.parser")
    names_tags = soup.find_all('h4', { "class": "card-title" })
    for i in names_tags:
        names.append(i.text)

    desc_tags = soup.find_all('p', { "class": "card-text" })
    for k in desc_tags:
        desc.append(k.text)

    imgs_tags = soup.find_all('img', { "class": "card-img-top" })
    for l in imgs_tags:
        images.append(l["src"])


data_array = []
for index,d in enumerate(names):
    dic = {
            'name': names[index],
            'description': desc[index],
            'imageURL': images[index], 
            'type': 'vegetable-juice',
            'price': math.floor(random.random() * 2000)
    }
    data_array.append(dic);

json_data = json.dumps(data_array, indent=2)
with open("data/vegetable-juices.json", "w") as file:
    file.write(json_data)
