from typing import Optional, Union


class OddsClientError(Exception):
    """Raised when the the response from the API does not return 200.
    
    Attributes:
        message -- the custom part of message the error displays
        status_code -- the response code
        reference -- the link to the appropraite resource
    """

    __DEFAULT_MESSAGE__ = "The Odds API did not return 200"
    __REFERENCE__ = "https://the-odds-api.com/liveapi/guides/v3/#overview"

    def __init__(self, status_code: str, 
                    reference: Optional[Union[str, None]] = None,
                    message: Optional[Union[str, None]] = None) -> None:
        if not reference:
            reference = OddsClientError.__REFERENCE__
        if not message:
            message = OddsClientError.__DEFAULT_MESSAGE__

        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.reference = reference


    def __str__(self) -> str:
        return (
            f"""[MESSAGE] -- {self.message}. """
            f"[STATUS CODE] -- {self.status_code} "
            f"[REFERENCE] -- {self.reference} "
        )

