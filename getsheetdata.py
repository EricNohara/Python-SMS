import getsheet
from datetime import date

START_DATE = date(2023, 12, 18)
today = date.today()

total_days_since = (today - START_DATE).days
weeks_since = total_days_since // 7
# WEEK AND DAY NUM IN CURRENT CYCLE
week_num = weeks_since + 1
day_num = total_days_since % 7

day_num_to_lift_num = {
    1: 1,
    2: -1,
    3: 2,
    4: -1,
    5: 3,
    6: 4,
    7: -1
}

sheet_by_week = {
    # MAP LINK TO SHEET TO CORRESPONDING WEEK IN PROGRAM
    1: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=0",
    5: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=1356405619",
    9: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=429567727",
    12: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=1035790153",
    16: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=378754300"
}


def format_sms_msg(week, day):
    lift_num = day_num_to_lift_num[day]
    print(lift_num)
    # If the current day in training cycle is not a lifting day, return string.
    if lift_num == -1:
        return "Today is a rest day."    

    # GET CORRECT SHEET BASED ON WEEKNUM
    sheet = getsheet.get_sheet_from_url(sheet_by_week[week])
    cur_sheet = sheet.loc[0 + ((lift_num - 1) * 6):(lift_num * 6) - 1]
    todays_lifts = list(filter(lambda e: e != "Null", cur_sheet.loc[:,"Exercise"].values))
    todays_weights = list(filter(lambda w: w != "Null", cur_sheet.loc[:,f"Week {week}"].values))
    print(todays_lifts, todays_weights)

format_sms_msg(week_num, day_num)
    


