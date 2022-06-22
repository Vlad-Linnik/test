import requests
from PIL import Image
from io import BytesIO


response = requests.get("https://randomfox.ca/floof")
print(response.status_code)
fox_image = response.json()['image']
print(fox_image)
response = requests.get(fox_image)
img = Image.open(BytesIO(response.content))
img.show()