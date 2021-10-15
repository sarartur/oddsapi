from types import SimpleNamespace
import re
import json

from .exceptions import OddsClientError

class Collection(SimpleNamespace):

    def __init__(self, **kwargs) -> None:
        clean_kwargs = {Collection.clean(key): value for key, value in kwargs.items()}
        SimpleNamespace.__init__(self, **clean_kwargs)

    @staticmethod
    def clean(string: str) -> str:
        string = re.sub(
            '[^0-9a-zA-Z_]', '', 
            re.sub('^[^a-zA-Z_]+', '', string)
        )
        return string
  
class BaseType(object):

    def __init__(self) -> None:
        pass

    _exclude_from_str = ["json", "text"]
    def __str__(self) -> str:
        items = (
            f"{k}={v!r}" for k, v in self.__dict__\
                .items() if k not in self.__class__._exclude_from_str)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __repr__(self) -> str:
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

class OddsApiResponse(BaseType):

    def __init__(self, response_text: str, headers) -> None:
        self._parse_response(response_text)
        self.text = response_text
        self._set_rate_info(headers)

    def _set_rate_info(self, headers):
        self.rate_info = dict(
            requests_remaining=headers['X-Requests-Remaining'],
            requests_used=headers['X-Requests-Used'])

    def _parse_response(self, response_text: str) -> None: 
        try:
            self._create_json_attr(response_text)
            self._create_object_attrs(response_text)
        except Exception as err:
            raise OddsClientError(
                status = 200,
                msg = "The server did not return a json response",
            ) from err
            
    def _create_json_attr(self, response_text: str) -> None:
        self.json = json.loads(response_text)

    def _create_object_attrs(self, response_text: str) -> None:
        attrs = json.loads(response_text, object_hook=lambda d: Collection(**d))
        self.__dict__.update(**attrs.__dict__)

class Resource(object):

    def __init__(self, uri, params, extra_kwargs=None) -> None:
        self.uri = uri
        self.params = params
        self.extra_kwargs = extra_kwargs or dict()