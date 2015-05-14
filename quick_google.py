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

def EventListHtml():
    Fname = 'EventList.html'
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    calendars = service.calendarList().list().execute()
    target_calendar_id = calendars['items'][0]['id']

    # ファイルオープン
    f = open(Fname, 'w')

    # ヘッダー
    f.write('''
   <html>
   <head></head>
   <body>
      <ul>\n''')

    #　イベント一覧取得
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    f.write('          <table border="1" cellpadding="1" cellspacing="1" class="event_list">\n')
    f.write('             <tr><th colspan="3" class="event_list">EventList(' + target_calendar_id + ')</th></tr>\n')
    f.write('             <tr><th class="tytle">TYTLE</th><th class="StrtTm">START</th><th class="EndTm">END</th></tr>\n')
    if not events:
        f.write('             <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></td><td class="noday">&nbsp;</td></tr>\n')
    for event in events:
        strtTm = event['start'].get('dateTime', event['start'].get('date'))
        endTm = event['end'].get('dateTime', event['end'].get('date'))
        tytle = event['summary']
        f.write('             <tr><td class="tytle">' + tytle + '</td><td class="StrtTm">' + strtTm + '</td><td class="EndTm">' + endTm +'</td></tr>\n')

    f.write('''          </table>''')

    # フッター
    f.write('''
       </ul>
   </body>
   </html>''')

    # 終了
    f.close()

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
        'start': {'date':''},
        'end': {'date':''},
        'summary': ''
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

def HoldayList(InputDt):
    credentials = get_credentials()
    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    # 祝祭日一覧取得
    events = service.events().list(calendarId='ja.japanese#holiday@group.v.calendar.google.com').execute()

    # 祝祭日一覧をソートして表示
    if InputDt == '5':
        # ファイルオープン
        f = open('HolidayList.html', 'w')

        # ヘッダー
        f.write('''
       <html><head>
       </head><body>
          <ul>\n''')

        f.write('          <table border="1" cellpadding="1" cellspacing="1" class="holiday_list">\n')
        f.write('             <tr><th colspan="2" class="holiday_list">休日一覧</th></tr>\n')
        f.write('             <tr><th class="Date">日付</th><th class="Name">名称</th></tr>\n')
        for item in sorted(events['items'], key=lambda item: item['start']['date']):
            f.write('             <tr><td class="Date">' + item['start']['date'] + '</td><td class="Name">' + item['summary'] + '</td></tr>\n')
        f.write('''          </table>''')

        # フッター
        f.write('''
          </ul>
       </body></html>''')

        f.close()

    else:
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
    InputDt = input('1:イベント一覧/2:イベント追加/3:イベント一覧(HTML)/4:祝祭日一覧/5:祝祭日一覧(HTML)：')
    if (InputDt == '1') | (InputDt == '2'):
        EventOpe(InputDt)
    elif InputDt == '3':
        EventListHtml()
    elif (InputDt == '4') | (InputDt == '5') :
        HoldayList(InputDt)
    else:
        print('unknown input data')