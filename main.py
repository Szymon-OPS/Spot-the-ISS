#------------------- IMPORTS AND CONSTANTS --------------------------------------------

import requests
from datetime import datetime

# Add lat and lon of desired observation location from which you intend
# to observe the ISS:
MY_LAT = 53.734089
MY_LON = 18.926979

#------------------- ISS POSITION -----------------------------------------------------

def is_iss_overhead():

    # Send request to external API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    
    # Exact exception will be raised if unsuccessful
    response.raise_for_status()

    # Get hold of response data
    data = response.json()
    
    # Get hold of latitude and longitude
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    
    # Check if ISS is +-5 degrees from your position (ensure visibility)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
        return True

#------------------- VISIBILITY IN MY POSITION ----------------------------------------

def is_night():
    # Store input parameters - same NAMES as in API documentation!
    # "formatted" specifies 12/24h format
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",
                            params=parameters)
    
    # Exact exception will be raised if unsuccessful
    response.raise_for_status()

    # Get hold of response data
    data = response.json()
    
    # Get hold of sunset/sunrise hour in 24h format
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    
    # Test
    # print(sunrise)
    # print(sunset)

    time_now = datetime.now()
    current_hour = int(time_now.hour)
    
    # Test
    # print(time_now.hour)
    
    if current_hour < sunrise or current_hour > sunset:
        return True
