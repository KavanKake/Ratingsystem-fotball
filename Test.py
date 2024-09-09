import requests
import json

# URL til API-endepunktet
url = "/Users/kavinlokeswaran/Documents/GitHub/Ratingsystem-fotball/La liga .json"

# Gjør en GET-forespørsel til APIet
response = requests.get(url)

# Sjekk om forespørselen var vellykket
if response.status_code == 200:
    # Hent data fra API som JSON
    data = response.json()

    # Print ut hele datasettet i en lesbar form
    print(json.dumps(data, indent=4))
else:
    print(f"Kunne ikke hente data. Statuskode: {response.status_code}")

