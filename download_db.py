import os
import io
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Set up
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'
DB_FILE_ID = '1YdeP9up1GxmvPtg1p710h0lruslIbq68'  # Replace this with your actual file ID
DEST_PATH = 'eod2.db'

def authenticate():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def download_file():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    request = service.files().get_media(fileId=DB_FILE_ID)
    fh = io.FileIO(DEST_PATH, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    print(f'Download complete: {DEST_PATH}')

if __name__ == '__main__':
    download_file()
