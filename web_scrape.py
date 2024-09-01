import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the property listing website
url = 'https://www.propertyfinder.ae/en/rent/properties-for-rent.html'

# Send a request to the website with a user-agent header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# Print the HTML content to verify the request is successful
print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store property data
property_data = []

# Find all property listings on the page
listings = soup.find_all('div', class_='card-list__item')  # Update the selector based on actual HTML structure
print(f"Found {len(listings)} listings")

for listing in listings:
    try:
        # Extract the property details
        rooms = listing.find('span', class_='property-card__rooms').text.strip()  # Update based on actual HTML structure
        area = listing.find('span', class_='property-card__area').text.strip()  # Update based on actual HTML structure
        property_type = listing.find('span', class_='property-card__type').text.strip()  # Update based on actual HTML structure
        property_usage = listing.find('span', class_='property-card__usage').text.strip()  # Update based on actual HTML structure
        rent_price = listing.find('span', class_='property-card__price-value').text.strip()  # Update based on actual HTML structure
        
        # Append the data to the list
        property_data.append({
            'Rooms': rooms,
            'Area': area,
            'Property Type': property_type,
            'Property Usage': property_usage,
            'Rent Price': rent_price
        })
        print(f"Added listing: {rooms}, {area}, {property_type}, {property_usage}, {rent_price}")
    except AttributeError:
        # Skip listings with missing data
        print("Missing data in listing, skipping...")
        continue

# Convert the list to a DataFrame
df = pd.DataFrame(property_data)

# Save the DataFrame to a CSV file
df.to_csv('property_listings.csv', index=False)

print("Data has been saved to property_listings.csv")

print(response.content)