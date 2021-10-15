import sys
sys.path.append('../')

from oddsapi import OddsApiClient
from app_secrets import API_KEY
from asyncio import gather

client = OddsApiClient(api_key=API_KEY)

response = client.retrieve_sports()
print(response.rate_info)

client.aio = True
cors = [client.retrieve_odds(
    sport_key=sport.key,
    region='us',
    mkt='spreads'
) for sport in response.data[:4]]
responses = client.loop.run_until_complete(gather(*cors))
print(len(responses))

