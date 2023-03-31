import news_converter_brrrrr
import requests
import json
from PIL import Image

# Set up the API endpoint
url = "https://api.openai.com/v1/images/generations"

# Set up the API key
api_key = "your_api_key"

# Set up the prompt (text description of the image you want to generate)
prompt = news_converter_brrrrr.news_story 

# Set up the request parameters
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "1024x1024",
    "response_format": "url"
}

# Send the request to the API
response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, data=data)

# Extract the URL of the generated image from the API response
image_url = json.loads(response.content)["data"][0]["url"]

# # Download the image
# image_response = requests.get(image_url)
# image_data = Image.open(BytesIO(image_response.content))

# Display the image
# image_data.show()
