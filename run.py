import gspread
from google.oauth2.service_account import Credentials

# The SCOPE lists APIs that the program should access in order to run
# This will not change
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Now we will access our love_sandwitches sheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Access data from the sheet
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)