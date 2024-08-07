# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Gets sales figures
    """
    while True:
        print("enter sales data")
        print("dtat should be 6 muns")
        print("eg: 23, 23, 23, 23\n")

        data_str = input("enter sales figures here")
    
        sales_data = data_str.split(",")
        

        if validate_data(sales_data):
            print("data is valid")
            break

    return sales_data


def validate_data(values):
    print(values)
    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you gave {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again.\n")
        return False

    return True


def update_sales_worksheet(data):
    """
    update sales worsheet
    """
    print("updating sales worksheet....\n")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print("sales worksheet updated \n")

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(data)