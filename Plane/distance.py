from math import radians, sin, cos, sqrt, atan2
from logoff import *

# Function to calculate the distance between two points on Earth
def haversine(lat1, lon1, alt1, lat2, lon2, alt2):
    r = 6371.0  # Radius of Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Calculate differences in latitude and longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    great_circle = r * c

    # Handle None values for altitude using default value of 0
    alt1 = alt1 or 0
    alt2 = alt2 or 0
    alt_diff = abs(alt2 - alt1) / 1000  # Convert to kilometers

    # Combine the great-circle distance and altitude difference
    real_distance = sqrt(great_circle**2 + alt_diff**2)

    return real_distance


# Function to find the closest pair of flights based on geographic coordinates
def find_closest_pair(flights):
    min_distance_km = float('inf')
    closest_pair = None # Place holder for the closest pair of flights

    # Compare all pairs of flights
    flight_count = len(flights)

    for i in range(flight_count):
        current_count_str_pre = '0000000' + str(i)
        current_count_str = current_count_str_pre[-1 * len(str(flight_count)):]

        completion_pct = round((i / flight_count) * 100., 2)

        logger.info('Processed {}/{} Flights ({}%)'.format(current_count_str, flight_count, completion_pct))

        for j in range(i + 1, flight_count):
            plane1, plane2 = flights[i], flights[j]
            lat1, lon1, alt1 = plane1[6], plane1[5], plane1[13]  # Latitude and Longitude for plane1
            lat2, lon2, alt2 = plane2[6], plane2[5], plane2[13]  # Latitude and Longitude for plane2

            # Skip planes with missing coordinates
            if None in (lat1, lon1, alt1, lat2, lon2, alt2):
                continue
            
            # Calculate the distance between the two planes
            distance_km = haversine(lat1, lon1, alt1, lat2, lon2, alt2)

            # Update the closest pair if the current distance is smaller
            if distance_km < min_distance_km:
                min_distance_km = distance_km
                closest_pair = (plane1, plane2)

    # Convert distance to feet
    min_distance_ft = min_distance_km * 3280.84
    return closest_pair, min_distance_ft
