
**House Board**
===========



# Product Overview
  This will be a message board, calendar, and reminder system for community houses. I would like it to be a one stop place for all the information needed to know whats going on at the house, both at the present and in the future. Private and public to do lists can be made for chores.

# Specific Functionality


## Main Page

- Shows upcoming events, the most recent public messages, notifications for current user, and links to every other page.  

## Calendar

Shows a calendar of events either by month or week.  

- Import:  

  Import a calendar to your personal calendar (as in not for the whole house calendar)

- View:  

  Click on an event to get more details. Description,

- Flag:

  Flag an event to receive notifications about it



To Do
------

Shows house wide and personal to do lists. Tasks can have due dates and be shared between multiple lists

- Add:  

  Add a task to a to do list, can be shared to the house wide list or other personal lists.

- Finish:  

  Mark a task as finished, also marks as finished on other lists if it is shared between multiple.



Private Messages
----------------

Private messages sent to the user.

 - Send:  

   Send a message to another account.

 - Erase:  

   Erase a message so it doesn't clutter inbox



Public Message Board
--------------------

   A list of messages for everyone to see

- Add:  

  Add a message to the public board

- Edit:  

  Edit one of your messages on the board

- Comment:  

  Add a comment to a message

- Notifications:

  Displays important information for current user. New private messages, new events added to calendar, flagged upcoming events, new tasks added to to do lists, tasks that are due or almost due.

- Go to:

  Clicking on a notification will take you to the relevant page for interacting with it.



Account Management
------------------

View and change account info and settings

- Change password:
  change your password



Sign up/Login
-------------

- Sign up:
  Create an account

- Login:
  Log in to your account

# Data Model
- Calendars:  

  Contains events, belongs to either a specific user or the entire house

- Events:  

  Start date/time, end date/time, description

- To do lists:  

  Contains tasks, belongs to either a specific user or the entire house

- Tasks:  

  Creation date, due date/time, who to remind, description, finished or not

- Board:  

  Contains public messages that everyone can see

- Public Messages:  

  Creation date, comments, account that created message, content, title, time last edited

- Private Message:  

  Content, subject, to, from, date sent

- Account:  

    username, password

- Notifications:

    link to appropriate page, date/time, content, read

# Technical Components

- Facebook integration:  

    Get event information for calendar events

- Google calendar integration:  

    see events on calendar from external google calendars, export house calendar to your personal external calendar(s)

- openweathermap:  

    Show current and forcasted weather

- Django:  

    create databases for user accounts, calendars and their events, todo lists and their tasks, message boards and their messages, the notification and private messages inboxes for users

# Schedule

1. Calendar backend
2. Calendar frontend
3. account creation and management
4. calendar import/export
5. to do lists
6. message boards
7. private messages
8. notifications

# Further Work

- Create a linux app as well as the web app:  

    This would allow me to install a touchscreen monitor somewhere publicly viewable in the house so that messages and reminders are visible in the physical space at all times. Have it run on my raspberry pi

- Create a phone app:  

    This would allow notifications to be pushed to a user's phone. It could also be set up to push reminders when the phone is at the actual house. This way, you could have a reminder to, for example, grab something from the house only come up when you are actually at the house.

- Media server:  

    allow for streaming/downloading media for viewing. Maybe have something like RetroPi for console emulation

- Recommendations:  

    Recommended places to go, primarily for guests who are staying over.

- Map integration:  

    show directions from house to a location from an event or task or a recommended place to go

- Drawn notes:  

    allow users to draw notes and leave them on the main page for others to see

- Guest Functionality:  

    give guests without an account some access. A guest specific message board perhaps, to leave notes for the inhabitants
