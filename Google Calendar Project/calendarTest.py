from __future__ import print_function
import datetime
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-02:00'      # PDT/MST/GMT-7

# evento = EventInput("","","","")

def pular_linhas(linhas_puladas):
    i = 0
    while i < linhas_puladas:
        print("")
        i += 1

def create_event():
    print('Qual o nome do evento?')
    #evento.name = raw_input()
    nome = raw_input()

    print('Qual a data do evento? (yyyy-mm-dd)')
    #evento.date = raw_input()
    data = raw_input()

    print('Qual a hora de inicio do evento? (xx:xx)')
    #evento.time += ("T" + raw_input() + ":00")
    inicio = ("T" + raw_input() + ":00%s")


    #print('Qual a duracao do evento?')
    #evento.time += ("+" + raw_input())
    print('Qual a hora de fim do evento? (xx:xx)')
    fim = ("T" + raw_input() + ":00%s")


    #evento.date_and_time = evento.date + evento.time


    EVENT = {
        'summary': nome,
        'start':  {'dateTime': (data + inicio) % GMT_OFF},
        'end':    {'dateTime': (data + fim) % GMT_OFF},
        'attendees': [
            #{'email': ''},
        ],
    }

    e = GCAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()
    pular_linhas(1)
    print('Evento criado')

def lookup_events(results):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = GCAL.events().list(calendarId='primary', timeMin=now,
                                        maxResults=results, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

print(chr(27) + "[2J")

while True:
    print("------------------- Bem vindo. -------------------")
    pular_linhas(1)
    print('Oque voce gostaria de fazer?')
    print(' 1-Criar evento')
    print(' 2-Ver seus proximos eventos')
    command = input()

    pular_linhas(2)


    if command == 1:
        create_event();
    elif command == 2:
        lookup_events(10);
    else:
        print("Comando invalido.")

    pular_linhas(2)
    #switch(command)
