import requests


class Download:
    """This class helps to download different embeddings for Nepali language"""

    def __init__(self):
        pass

    def download_file_from_google_drive(self, id, destination):
        """Download Nepali embedding file which is in gooogle drive.
        
        Arguments:
            id {string} -- unique id;represent file in google drive
            destination {string} -- filename where the content is to be written

            eg: id: '1KnAZ2Eeqwz3S9VrAuzTLWysAaRB6Ch7e'
                destination: 'abc.txt'
        
        Returns:
            [type] -- [description]
        """

        def get_confirm_token(response):
            for key, value in response.cookies.items():
                if key.startswith('download_warning'):
                    return value

            return None

        def save_response_content(response, destination):
            CHUNK_SIZE = 32768

            with open(destination, "wb") as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)

        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={'id': id}, stream=True)
        token = get_confirm_token(response)

        if token:
            params = {'id': id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        save_response_content(response, destination)

    def __str__(self):
        return "Required to Download embedding from weblink. Make sure your internet is working."
