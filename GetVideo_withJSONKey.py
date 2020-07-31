import os

# import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.client import Credentials
import httplib2

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    with open('/home/Foroozan/Desktop/SpeechToText/youtube_key.json','rb') as f:
        json_content = f.read()

    credentials = Credentials.new_from_json(json_content)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, http=credentials.authorize(httplib2.Http()))

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UCkCrYodUaJNbfS1cWhCyhGg",
        managedByMe=False
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
