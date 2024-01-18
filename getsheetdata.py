import getsheet
from datetime import date

class FormatSheet:
    def __init__(self, start_date):
        """
        Initiate format sheet with a given start date of a workout program.

        Important arguments:
        start_date -- start date of your workout program. Replace with your correct program start date.
        day_num_to_lift_num -- dictionary which defines which day corresponds to a lifting day in a given program. Rest days are defined as -1.
        sheet_by_week -- dictionary defining the corresponding google sheet link for week ranges in a given program. Replace these or if all workout data is on one sheet, disregard.
        """
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
        """
        Arguments:
        lifts -- an array of strings containing all of the non-null exercise rows in a given day.
        weights -- an array of strings containing all of the non-null weights/reps rows in a given day.

        Returns an array containing formatted strings with the lifts and weights concatenated.
        """
        pairs = []
        for i in range(len(lifts)):
            if i < len(lifts) - 1:
                pairs.append(f"{lifts[i]}: {weights[i]}\n")
            else:
                pairs.append(f"{lifts[i]}: {weights[i]}")
        return pairs

    def generate_fstring_from_pairlist(self, pairs):
        """
        Arguments:
        pairs -- an array of formatted strings returned from calling the generate_lift_weight_pairs() function on a lifts and weights array.

        Returns a formatted string from the pairs array which containes a nicely formatted list of today's workout.
        """
        msg = "Todays Workout:\n"
        for p in pairs:
            msg += p
        return msg
    
    def format_sms_msg(self):
        """
        Returns a string with the corresponding workout for a given day.

        If today is not a lifting day, return a string saying today is a rest day.
        Otherwise, return the formatted string by calling generate_lift_weight_pairs() and generate_fstring_from_pairlist() on defined values.
        """
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
