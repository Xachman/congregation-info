import creds
from googleapiclient.discovery import build
import logger
from datetime import datetime
import time

SPREADSHEET_ID = "1Jb_O1CtFU7l20hUi0dmUy_7nPVU0dqH0N89svBH-uIg"
SHEET_ID="0"
RANGE_NAME = 'Sheet1!A2:E'

def getToday():
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
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            currentDate = datetime.now()
            startDate = datetime.strptime(row[0], "%Y-%m-%d").date()
            endDate = datetime.strptime(row[1], "%Y-%m-%d").date()
            logger.log(currentDate)
            logger.log(startDate)
            logger.log(endDate)

            if currentDate.timestamp() > time.mktime(startDate.timetuple()) and currentDate.timestamp() < time.mktime(endDate.timetuple()):
                return {"group": row[2], "type": row[3]}

    return {}


    