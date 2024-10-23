import requests

    # Define the API endpoint URL
url = 'https://www.fotmob.com/api/matchDetails'
    # Make a GET request to the API endpoint using requests.get()
response = requests.get(url, params={
    'matchId': 4506770})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    posts = response.json()
    print(posts)  # Print the posts
else:
    print('Error:', response.status_code)

