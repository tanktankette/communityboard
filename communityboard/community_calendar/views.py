from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient.discovery import build
from datetime import date, timedelta
from calendar import monthrange, weekday
from .calendarfunctions import *


def index(request, month=0, year=0):

    today = date.today()

    if month:
        if not year:
            year = today.year
        today = date(int(year), int(month), 1)

    past_days, days_in_month = monthrange(today.year, today.month)
    last_day = weekday(today.year, today.month, days_in_month)
    last_day = 5 - last_day
    if last_day == -1:
        last_day = 6

    past_days += 1
    if past_days + last_day < 8:
        last_day += 7

    calendar_start = today - timedelta(today.day + past_days - 1)
    calendar_end = today + timedelta(days_in_month - today.day + last_day)

    scopes = ['https://www.googleapis.com/auth/calendar']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/home/tanktankette/Downloads/Community Calendar-eac475d17749.json', scopes=scopes
    )

    http_auth = credentials.authorize(Http())

    calendar = build('calendar', 'v3', http=http_auth)

    response = calendar.events().list(calendarId='ministryofmagicpdx@gmail.com',
                                      timeMin=f'{calendar_start}T00:00:00-07:00',
                                      timeMax=f'{calendar_end}T00:00:00-07:00',
                                      orderBy='startTime',
                                      singleEvents=True).execute()['items']

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
                    event_dict[day].append(event)
                else:
                    event_dict[day] = [event]

    day_list = [calendar_start]

    while day_list[-1] != calendar_end:
        day_list.append(day_list[-1] + timedelta(1))

    day_list = [day_list[0:7], day_list[7:14], day_list[14:21], day_list[21:28], day_list[28:35], day_list[35:42]]

    context_dict = {'events': event_dict,
                    'weeks': day_list,
                    'today': today}

    return render(request, 'community_calendar/index.html', context_dict)
