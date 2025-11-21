from oauth2client.service_account import ServiceAccountCredentials

fsm_scope = 'https://www.googleapis.com/auth/firebase.messaging'

class Google_api_controller:
    def __init__(self):
        super().__init__()
    
    def get_access_token(self):
        """Retrieve a valid access token that can be used to authorize requests.

        :return: Access token.
        """
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'keystore/service-account.json', fsm_scope)
        access_token_info = credentials.get_access_token()
        return access_token_info