from __future__ import print_function
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1dqtrISDomatlZDICcZmL1q_qfmE8tZ3uDq9eMmeypVw'


def get_last_index():
    RANGE_NAME = 'A:A'

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    return len(values)


def parse_month_and_day(date):
    months = {
        "Oca": "01",
        "Şub": "02",
        "Mar": "03",
        "Nis": "04",
        "May": "05",
        "Haz": "06",

        "Tem": "07",
        "Ağu": "08",
        "Eyl": "09",
        "Eki": "10",
        "Kas": "11",
        "Ara": "12",
    }
    date = date.split(' ')
    month = months.get(date[0])
    day = date[1]
    return (month, day)


def parse_hour(time):
    if "-" in time:
        _time = time.split('-')
        if ":" in _time[0]:
            __time = _time[0].split(':')
        else:
            __time = _time[0].split('.')
    else:
        if ":" in time:
            __time = time.split(':')
        else:
            __time = time.split('.')
    hour = __time[0]
    minute = __time[1]
    return (hour, minute)


creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

####################################
############   INIT   ##############
####################################

index = get_last_index()


def get_sheets_data():

    RANGE_NAME = f'A2:F{index}'
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in range(index-1):
            for column in range(6):
                if len(values[row]) < 6:
                    values[row].extend([''] * (6 - len(values[row])))
                    # print(values[row][column])
                # else:
                    # print(values[row][column])
    return values

    # if values[row][0] is not None and values[row][0] is not '':
    #     print(parse_month_and_day(values[row][0]))
    #     data = parse_month_and_day(values[row][0])
    # if values[row][4] is not None and values[row][4] is not '':
    #     print(parse_hour(values[row][4]))
    #     hour_minute = parse_hour(values[row][4])
    # Event.objects.create(
    #     author='9e89a295-d7d1-4ed8-a0d1-6039240b0c56',
    #     title=values[row][3],
    #     event_url=values[row][5],
    #     venue=values[row][2],
    #     community=values[row][1],
    #     desc=values[row][3],
    #     category=1,
    #     date=timezone.datetime(
    #         year=2020, month=data[0], day=data[1],
    #         hour=hour_minute[0], minute=hour_minute[1]
    #     )
    # )
