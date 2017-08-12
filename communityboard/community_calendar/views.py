from django.shortcuts import render
from calendar import monthrange, weekday
from .calendarfunctions import *
from datetime import timedelta

# TODO: EVENT CREATION AND MODIFICATION
# TODO: CREATE TAG LANGUAGE FOR EVENT DESCRIPTIONS
#   maybe just an ignore tag for tasks and events that are in this database
# TODO: MESSAGE BOARD
#   regular and pinned messages
# TODO: LANDING PAGE
# TODO: MEDIA SERVER
# TODO: PHONE APP



def index(request, month_year=''):

    if month_year:
        month, year = month_year.split("-")
        today = date(int(year), int(month), 1)
    else:
        today = date.today()

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

    calendar = auth_calendar()

    response = calendar.events().list(calendarId='ministryofmagicpdx@gmail.com',
                                      timeMin=f'{calendar_start}T00:00:00-08:00',
                                      timeMax=f'{calendar_end}T00:00:00-07:00',
                                      orderBy='startTime',
                                      singleEvents=True).execute()['items']

    event_dict = parse_event_list(response)

    day_list = [calendar_start]
    while day_list[-1] != calendar_end:
        day_list.append(day_list[-1] + timedelta(1))
    day_list = [day_list[0:7], day_list[7:14], day_list[14:21], day_list[21:28], day_list[28:35], day_list[35:42]]

    context_dict = {'events': event_dict,
                    'weeks': day_list,
                    'today': today}

    return render(request, 'community_calendar/index.html', context_dict)


def event_detail(request, event_id):

    calendar = auth_calendar()
    response = calendar.events().get(calendarId='ministryofmagicpdx@gmail.com',
                                     eventId=event_id).execute()
    context_dict = parse_event(response)

    if 'recurringEventId' in response:
        context_dict['recurringEventId'] = response['recurringEventId']
        response = calendar.events().get(calendarId='ministryofmagicpdx@gmail.com',
                                         eventId=response['recurringEventId']).execute()
        context_dict['recurrence'] = response['recurrence']

    return render(request, 'community_calendar/event.html', context_dict)
