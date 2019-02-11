from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class EventInput:
    def __init__(self, name, date, time, date_input):
        self.name = name
        self.date = date
        self.time = time
        self.date_input = date_input

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    # EventInput.name = name
    # print(EventInput.name)

if __name__ == '__main__':
    main()

# Programa começa aki
evento = EventInput("",0,0,"")

print('Qual o nome do evento?')
evento.name = raw_input()

print('Qual o ano do evento?')
evento.date_input = raw_input()

print('Qual o mes do evento?')
evento.date_input += ("-" + raw_input())

print('Qual o dia do evento?')
evento.date_input += ("-" + raw_input())

print(evento.date_input)
