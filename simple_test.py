import requests
import json

# Your credentials
TOKEN = "eca0e911fee22a56532bd9b127d45e3c23e84e49829cf7140befa2349f9d5b7e"
SITE_ID = "64e7c16bddef7563aa632f3d"

# Setup headers with API version
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_api():
    print("Testing Webflow API access...")
    
    # Test different endpoints
    endpoints = [
        f"https://api.webflow.com/sites/{SITE_ID}",  # v1 site info
        f"https://api.webflow.com/v2/sites/{SITE_ID}",  # v2 site info
        f"https://api.webflow.com/sites/{SITE_ID}/domains"  # domains
    ]
    
    for url in endpoints:
        print(f"\nTesting URL: {url}")
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
    # Test publish endpoint (POST request)
    publish_url = f"https://api.webflow.com/sites/{SITE_ID}/publish"
    print(f"\nTesting publish URL: {publish_url}")
    publish_response = requests.post(publish_url, headers=headers)
    print(f"Publish Status Code: {publish_response.status_code}")
    print(f"Publish Response: {json.dumps(publish_response.json(), indent=2)}")

if __name__ == "__main__":
    test_api()