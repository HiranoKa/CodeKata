__author__ = 'le-user'
# -*- coding: utf-8 -*-

"""A quickstart example showing usage of the Google Calendar API."""
import datetime
import os

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools
import time

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

#SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calendar API Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-api-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def InputDate(wkDate = ''):
    if wkDate == '':
        InpTytle = '開始日を入力してください'
    else:
        InpTytle = '終了日を入力してください'
    InputDate = input(InpTytle + '(yyyy-mm-dd) : ')
    if InputDate == "":
        if wkDate == "":
            tDateTime = datetime.datetime.now()
            InputDate = tDateTime.strftime('%Y-%m-%d')
        else:
            tDateTime = datetime.datetime.strptime(wkDate, '%Y-%m-%d')
            tDateTime += datetime.timedelta(days=1)
            InputDate = tDateTime.strftime('%Y-%m-%d')
    else:
        tDateTime = datetime.datetime.strptime(InputDate, '%Y-%m-%d')
        InputDate = tDateTime.strftime('%Y-%m-%d')
    print(InputDate)
    return InputDate

def EventList(service):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def EventAdd(service):
    event = {
        'start': {'date':'2015-05-14'},
        'end': {'date':'2015-05-15'},
        'summary': 'event_from_api'
    }

    Tytle = input('タイトルを入力 : ')
    if Tytle != "":
        event['summary'] = Tytle
        StrtDate = InputDate('')
        EndDate = InputDate(StrtDate)
        if (StrtDate != '') & (EndDate != ''):
            event['start']['date'] = StrtDate
            event['end']['date'] = EndDate
            print('Input event into Google Calendar')
            calendars = service.calendarList().list().execute()
            target_calendar_id = calendars['items'][0]['id']
            created_event = service.events().insert(calendarId=target_calendar_id, body=event).execute()
        else:
            print('開始日または終了日を入力してください！')
    else:
        print('タイトルを入力してください！！')

def EventOpe(InputDt):
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    if InputDt == '1':
        #10 events on the user's calendar
        EventList(service)
    elif InputDt == '2':
        # event set
        EventAdd(service)
        EventList(service)
    else:
        print('unknown input data')

def HoldayList():
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    # 祝祭日一覧取得
    events = service.events().list(calendarId='ja.japanese#holiday@group.v.calendar.google.com').execute()

    # 祝祭日一覧をソートして表示
    print('Getting the holiday list')
    for item in sorted(events['items'], key=lambda item: item['start']['date']):
        print( u'{0}\t{1}'.format(item['start']['date'], item['summary']))

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    InputDt = input('1:イベント一覧/2:イベント追加/3祝祭日一覧：')
    if (InputDt == '1') | (InputDt == '2'):
        EventOpe(InputDt)
    elif InputDt == '3':
        HoldayList()
    else:
        print('unknown input data')