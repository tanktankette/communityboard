from datetime import date, tzinfo, timedelta, time
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient.discovery import build


def parse_iso(iso):
    iso = map(lambda x: int(x), iso.split('-'))
    return date(*iso)


def parse_event(event):
    event_dict = {'summary': event['summary'],
                  'link': event['htmlLink'],
                  'id': event['id']}

    if 'date' in event['start']:
        event_dict['date'] = parse_iso(event['start']['date'])
    elif 'dateTime' in event['start']:
        event_dict['date'] = parse_iso(event['start']['dateTime'][0:10])
        start_time = map(lambda x: int(x), event['start']['dateTime'][11:19].split(':'))
        end_time = map(lambda x: int(x), event['end']['dateTime'][11:19].split(':'))
        event_dict['start_time'] = time(*start_time)
        event_dict['end_time'] = time(*end_time)

    return event_dict


def parse_event_list(response):
    event_dict = {}
    for event in response:
        day = ''
        if 'start' in event:
            if 'date' in event['start']:
                day = parse_iso(event['start']['date'])
            elif 'dateTime' in event['start']:
                day = parse_iso(event['start']['dateTime'][0:10])
            if day:
                if day in event_dict:
                    event_dict[day].append(parse_event(event))
                else:
                    event_dict[day] = [parse_event(event)]
    return event_dict


def auth_calendar():
    scopes = ['https://www.googleapis.com/auth/calendar']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/home/tanktankette/Downloads/Community Calendar-eac475d17749.json', scopes=scopes
    )

    http_auth = credentials.authorize(Http())

    return build('calendar', 'v3', http=http_auth)
