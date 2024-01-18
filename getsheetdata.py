import getsheet
from datetime import date

class FormatSheet:
    def __init__(self, start_date):
        self.today = date.today()
        self.start_date = start_date
        self.total_days_since = (self.today - self.start_date).days
        self.weeks_since = self.total_days_since // 7
        self.week_num = self.weeks_since + 1
        self.day_num = self.total_days_since % 7
        self.day_num_to_lift_num = {
            1: 1,
            2: -1,
            3: 2,
            4: -1,
            5: 3,
            6: 4,
            7: -1
        }
        self.sheet_by_week = {
            # MAP LINK TO SHEET TO CORRESPONDING WEEK IN PROGRAM
            1: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=0",
            5: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=1356405619",
            9: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=429567727",
            12: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=1035790153",
            16: "https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit#gid=378754300"
        }

    def generate_lift_weight_pairs(self, lifts, weights):
        pairs = []
        for i in range(len(lifts)):
            pairs.append(f"{lifts[i]}: {weights[i]}\n")
        return pairs

    def generate_fstring_from_pairlist(self, pairs):
        msg = "Todays Workout:\n"
        for p in pairs:
            msg += p
        return msg
    
    def format_sms_msg(self):
        lift_num = self.day_num_to_lift_num[self.day_num]
        # If the current day in training cycle is not a lifting day, return string.
        if lift_num == -1:
            return "Today is a rest day."    

        # GET CORRECT SHEET BASED ON WEEKNUM
        sheet = getsheet.get_sheet_from_url(self.sheet_by_week[self.week_num])
        cur_sheet = sheet.loc[0 + ((lift_num - 1) * 6):(lift_num * 6) - 1]
        todays_lifts = list(filter(lambda e: e != "Null", cur_sheet.loc[:,"Exercise"].values))
        todays_weights = list(filter(lambda w: w != "Null", cur_sheet.loc[:,f"Week {self.week_num}"].values))
        lift_weight_pairs = self.generate_lift_weight_pairs(todays_lifts, todays_weights)
        msg = self.generate_fstring_from_pairlist(lift_weight_pairs)
        return msg
    
format_sheet = FormatSheet(date(2023, 12, 18))
print(format_sheet.format_sms_msg())