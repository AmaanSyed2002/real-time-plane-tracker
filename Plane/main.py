# main.py

from plane import plane
from data import fetch_planes
from distance import find_closest_pair
from logoff import logger

def main():
    # Fetch flight data from the API
    logger.info('Fetching Flights...')
    flights = fetch_planes()
    logger.info('Flight Fetching Completed!')

    if flights:
        # Find the closest pair of flights and their distance in feet
        closest_pair, distance_ft = find_closest_pair(flights)
        
        if closest_pair:
            # Unpack the closest pair of planes
            plane1, plane2 = closest_pair
            
            # Extract callsign (unique identifier) or default to "Unknown" if missing
            callsign1 = plane1[1] if plane1[1] is not None else "Unknown"
            icao1 = plane1[0]
            lat1, lon1, alt1, time1 = plane1[6], plane1[5], plane1[13], plane1[3]  # Latitude and Longitude for plane 1
            
            callsign2 = plane2[1] if plane2[1] is not None else "Unknown"
            icao2 = plane2[0]
            lat2, lon2, alt2, time2 = plane2[6], plane2[5], plane2[13], plane2[3]  # Latitude and Longitude for plane 2

            # Print details of the closest planes and their distance
            print(f"Plane 1: {callsign1} ({lat1}, {lon1}, {alt1}, {time1})\nPlane 2: {callsign2} ({lat2}, {lon2}, {alt2}, {time2})\nDistance: {distance_ft:.2f} FT")
            print(f"https://globe.adsb.fi/?icao={icao1},{icao2}")
        else:
            #Due to missing or invalid data
            logger.error('No Closest Pair Found')
    else:
        ## No flight data retrieved from the API
        logger.error('No Flight Data Available')

# Entry point of the program
if __name__ == "__main__":
    main()
