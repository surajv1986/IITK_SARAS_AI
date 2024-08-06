import googlemaps

# Replace with your actual Google Maps API key
api_key = "AIzaSyCPABCvyr3vC-EMRqTJbVTRvMyz5c0y_9k"

gmaps = googlemaps.Client(key=api_key)

# Geocode an address
geocode_result = gmaps.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

# Extract latitude and longitude
lat = geocode_result[0]["geometry"]["location"]["lat"]
lng = geocode_result[0]["geometry"]["location"]["lng"]

print(f"Latitude: {lat}, Longitude: {lng}")

# Find nearby places
places_result = gmaps.places_nearby(
    location=(lat, lng), radius=1000, type="restaurant"
)

# Print the names of nearby restaurants
for place in places_result["results"]:
    print(place["name"])
