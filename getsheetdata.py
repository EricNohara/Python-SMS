import getsheet

url = 'https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=0'

week = 3
day = "Monday"

lifting_days = {
    "Monday": 1,
    "Tuesday": -1,
    "Wednesday": 2,
    "Thursday": -1,
    "Friday": 3,
    "Saturday": 4,
    "Sunday": -1
}

print(getsheet.get_sheet_from_url(url))