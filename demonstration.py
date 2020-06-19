from oddsapi import OddsClient

#get your Api key at https://the-odds-api.com/
API_KEY = "Your Api Key Here"

client = OddsClient(api_key=API_KEY)

sports = client.retrieve_sports()

print(sports)

#The information on used and remianing requests is avaliable only 
#after at least one request has been sent to the API
print(f"Requests Remaining: {client.requests_remaining}")
print(f"Requests Used: {client.requests_used}")


odds = client.retrieve_odds(
    sport_key='americanfootball_ncaaf',
    region='us',
    mkt='spreads'
)

print(odds)

print(f"Requests Remaining: {client.requests_remaining}")
print(f"Requests Used: {client.requests_used}")