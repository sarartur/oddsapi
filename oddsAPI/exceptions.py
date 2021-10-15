class OddsClientError(Exception):

    default_msg = "The Odds API did not return 200"
    reference = "https://the-odds-api.com/liveapi/guides/v3/#overview"

    def __init__(self, status, reference=None, msg=None) -> None:
        self.reference = reference or OddsClientError.reference
        self.msg = msg or OddsClientError.default_msg
        self.status = status
    
    def __str__(self):
        return ("OddsApi did not return 200. "
            f"Status Code: {self.status}. "
            f"Msg: {self.msg}. "
            f"Reference: {self.reference}.")
