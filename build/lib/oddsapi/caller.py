import urllib3
import certifi
import json
from typing import List, Dict, Optional
from urllib.parse import urlencode

from oddsapi.errors import OddsClientError


class OddsClient(object):

    __HOST__ = "https://api.the-odds-api.com"
    https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        

    def _set_requests_info(self, headers: Dict) -> None:
        self.requests_remaining = headers['X-Requests-Remaining']
        self.requests_used = headers['X-Requests-Used']


    def retrieve_sports(self) -> List:
        """Public method that retrieves a list of in-season sports"""

        URL_EXTENSION = "/v3/sports/"
        r = OddsClient.https.request(
            method='GET',
            url = OddsClient.__HOST__ + URL_EXTENSION + '?' + urlencode({
                "apiKey": self.api_key
            }), 
        )
        response_body = json.loads(r.data.decode('utf-8'))
        if r.status != 200 and not response_body['success']:
            if 'status' in response_body and 'msg' in response_body:
                raise OddsClientError(status_code = r.status, message=f"{response_body['status']}; {response_body['msg']}")
            raise OddsClientError(status_code = r.status)

        self._set_requests_info(r.headers)
        return response_body['data']


    def retrieve_odds(self, sport_key: str, region: str, mkt: Optional[str] = 'h2h') -> List:
        """Public method that retrieves  a list of upcoming and live games with recent odds 
        for a given sport, region and market
        
        Parameters:
            sport -- "The sport key obtained from calling the /sports method"
            region -- "Determines which bookmakers are returned.
            mkt -- Determines which odds market is returned
        """

        URL_EXTENSION = "/v3/odds/"
        r = OddsClient.https.request(
            method='GET',
            url = OddsClient.__HOST__ + URL_EXTENSION + '?' + urlencode({
                "apiKey": self.api_key,
                "sport": sport_key,
                "region": region,
                "mkt": mkt
            }), 
        )
        response_body = json.loads(r.data.decode('utf-8'))
        if r.status != 200 and not response_body['success']:
            if 'status' in response_body and 'msg' in response_body:
                raise OddsClientError(status_code = r.status, message=f"{response_body['status']}; {response_body['msg']}")
            raise OddsClientError(status_code = r.status)

        self._set_requests_info(r.headers)
        return response_body['data']



    
   

