import requests
import json

# Your credentials
TOKEN = "eca0e911fee22a56532bd9b127d45e3c23e84e49829cf7140befa2349f9d5b7e"
SITE_ID = "64e7c16bddef7563aa632f3d"
DOMAIN = "maine-mountain-moccasin.webflow.io"  # Your Webflow domain

# Setup headers for v2 API
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_api():
    print("Testing Webflow API v2 access...")
    
    # Get site info using v2 API
    site_url = f"https://api.webflow.com/v2/sites/{SITE_ID}"
    print(f"\nGetting site info: {site_url}")
    response = requests.get(site_url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Try publish with domain specified
    publish_url = f"https://api.webflow.com/sites/{SITE_ID}/publish"
    publish_data = {
        "domains": [DOMAIN]
    }
    print(f"\nTesting publish to domain {DOMAIN}")
    publish_response = requests.post(
        publish_url, 
        headers=headers,
        json=publish_data
    )
    print(f"Publish Status Code: {publish_response.status_code}")
    print(f"Publish Response: {json.dumps(publish_response.json(), indent=2)}")

if __name__ == "__main__":
    test_api()