from __future__ import print_function
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

GMT_OFF = '-03:00'      # PDT/MST/GMT-7

# evento = EventInput("","","","")

print('Qual o nome do evento?')
#evento.name = raw_input()
nome = raw_input()

print('Qual o ano do evento?')
#evento.date = raw_input()
data = raw_input()

print('Qual o mes do evento?')
#evento.date += ("-" + raw_input())
data += ("-" + raw_input())

print('Qual o dia do evento?')
#evento.date += ("-" + raw_input())
data += ("-" + raw_input())

print('Qual a hora de inicio do evento?')
#evento.time += ("T" + raw_input() + ":00")
inicio = ("T" + raw_input() + ":00%s")


#print('Qual a duracao do evento?')
#evento.time += ("+" + raw_input())
print('Qual a hora de fim do evento?')
fim = ("T" + raw_input() + ":00%s")

#evento.date_and_time = evento.date + evento.time


EVENT = {
    'summary': nome,
    'start':  {'dateTime': (data + inicio) % GMT_OFF},
    'end':    {'dateTime': (data + fim) % GMT_OFF},
    'attendees': [
        {'email': 'beatris.fgsantos@gmail.com'},
    ],
}

e = GCAL.events().insert(calendarId='primary',
        sendNotifications=True, body=EVENT).execute()
