<img src="https://img.shields.io/github/issues/sarartur/oddsapi">  <img src="https://img.shields.io/github/forks/sarartur/oddsapi">   <img src="https://img.shields.io/github/stars/sarartur/oddsapi">   <img src="https://img.shields.io/github/license/sarartur/oddsapi">
# The Odds-Api
### Installation
The package requires Python 3.7 or higher.
Install latest version from PyPI: `pip install oddsapi`
### Description
The Odds-API provides sports odds data for loads of sports from bookmakers around the world. Get your free API key [here](https://the-odds-api.com/).
### Usage
Please refer to [documentation](https://the-odds-api.com/liveapi/guides/v3/) for detailed instructions for The Odds-Api.

To start using the wrapper import and initialize the `OddsApiClient` from the package. 
``` python
from oddsapi import OddsApiClient
from app_secrets import API_KEY

client = OddsApiClient(api_key=API_KEY)
response = client.retrieve_sports()
```
The response is a custom object that stores the data in nested namespaces and dictionary format.
```python
response.data[0]

>>> Collection(active=True, 
        details='US College Football', 
        group='American Football', 
        has_outrights=False, 
        key='americanfootball_ncaaf', 
        title='NCAAF')

#alternatively
response.json['data'][0]
>>> {'key': 'americanfootball_ncaaf', 
        'active': True, 
        'group': 'American Football', 
        'details': 'US College Football', 
        'title': 'NCAAF', 
        'has_outrights': False}

response.rate_info
>>> {'requests_remaining': '479', 'requests_used': '21'}
```
The client also be configured to work with `asyncio`.

```python
from asyncio import gather

client.aio = True
cors = [client.retrieve_odds(
    sport_key=sport.key,
    region='us',
    mkt='spreads'
) for sport in response.data[:4]] 
responses = client.loop.run_until_complete(gather(*cors))
```
Keep in mind that `rate_info` will not be recorded in order.
### Contact
Email me at sarartur.ruk@gmail.com or open a new [Issue](https://github.com/sarartur/oddsapi/issues) on Github.

