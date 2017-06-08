import requests

response = requests.get("https://cdph.data.ca.gov/api/views/6tej-5zx7/rows.json?accessType=DOWNLOAD")

print(response.status_code)
