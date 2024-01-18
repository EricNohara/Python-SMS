import getsheet
from datetime import date

START_DATE = date(2023, 12, 17)
today = date.today()

total_days_since = (today - START_DATE).days
weeks_since = total_days_since // 7
# WEEK AND DAY NUM IN CURRENT CYCLE
week_num = weeks_since + 1
day_num = total_days_since % 7

print(f"Week {week_num}, Day {day_num}")

day_num_to_lift_num = {
    1: 1,
    2: -1,
    3: 2,
    4: -1,
    5: 3,
    6: 4,
    7: -1
}

print(day_num_to_lift_num[day_num])



url = 'https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=0'

cur_sheet = getsheet.get_sheet_from_url(url)

print(cur_sheet.loc[0:5])
    


