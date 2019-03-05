import creds
from googleapiclient.discovery import build
import logger
from datetime import datetime
import time
import os


SPREADSHEET_ID = "1Jb_O1CtFU7l20hUi0dmUy_7nPVU0dqH0N89svBH-uIg"
SHEET_ID="0"
RANGE_NAME = 'Sheet1!A2:E'

def getToday():
    os.environ['TZ'] = 'US/Eastern'
    c = creds.get()
    service = build('sheets', 'v4', credentials=c)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        logger.log('No data found.')
    else:
        currentDate = datetime.now()
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            startDate = datetime.strptime(row[0], "%Y-%m-%d")
            endDate = datetime.strptime(row[1]+" 23:59:59", "%Y-%m-%d %H:%M:%S")
            logger.log(time.mktime(startDate.timetuple()))
            logger.log(time.mktime(endDate.timetuple()))

            if currentDate.timestamp() > time.mktime(startDate.timetuple()) and currentDate.timestamp() < time.mktime(endDate.timetuple()):
                return {"group": row[2], "type": row[3]}

    return {}


    