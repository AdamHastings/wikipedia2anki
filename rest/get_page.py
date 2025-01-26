import requests
import json

# Wikipedia API URL
# url = "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Homo_habilis&formatversion=2"
url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Homo_habilis&explaintext=1&formatversion=2"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    
    # Save the JSON data to a file
    with open("wikipedia_data.json", "w") as file:
        json.dump(data, file, indent=4)  # `indent=4` formats the JSON nicely
    
    print("JSON data saved to 'wikipedia_data.json'")
else:
    print(f"Error: {response.status_code}")