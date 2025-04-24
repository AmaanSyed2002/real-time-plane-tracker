import requests
import time
from logoff import logger  
from distance import haversine  

def process_results(results, now, airport_coords=None):
    
    logger.info('Pre-Processing: {} Entries'.format(len(results)))

    cleaned_results = []

    for d in results:
        clean = True

        # Test if time data exists and is not stale
        if d[3] is None or d[4] is None:
            clean = False
        else:
            if abs(d[3] - d[4]) > 1.0:  
                clean = False

            # Only planes that have reported in the last 45 seconds
            if now - d[3] > 45:  
                clean = False

        # Dropping any planes on the ground
        if d[8] is True:
            clean = False

        #The checking way to see if a plane is 5km from airport to avoid the airport.
        if clean and airport_coords:
            lat, lon, alt = d[6], d[5], d[13]
            for airport, (a_lat, a_lon) in airport_coords.items():
                airport_dist = haversine(lat, lon, alt, a_lat, a_lon, 0)
                if airport_dist < 5:   #this the km if its smaller its gets avoided. 
                    clean = False
                    logger.info(f"Plane near airport {airport} excluded: {d}")

        if clean:
            cleaned_results.append(d)

    for d in cleaned_results:
        d[0] = d[0].replace(' ', '')
        d[1] = d[1].replace(' ', '')

    logger.info('Post-Processing: {} Entries'.format(len(cleaned_results)))
    return cleaned_results


def fetch_planes():
    url = "https://opensky-network.org/api/states/all"
    now = int(time.time())

    logger.info('Collecting data from OpenSky Network...')
    response = requests.get(url)
    logger.info('OpenSky Network Collection Complete!')

    # Check if the request was successful and gets extracts the states data 
    if response.status_code == 200: 
        return(process_results(response.json().get("states", []), now))
    else:
        logger.error('Failed to Fetch Data - Status Code: {}'.format(response.status_code))
        return []

