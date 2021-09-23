#------------------- IMPORTS AND CONSTANTS --------------------------------------------

import requests

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
