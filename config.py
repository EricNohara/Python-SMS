from datetime import date
import os

number = "6363179533"   # Replace with your phone number.
provider = "AT&T"       # Replace with correct phone provider, match with keys in dictionary provided in providers.py file.
sender_credentials = ("eric.noharaleclair@gmail.com", "ujct wmrm kbjl pgun")       # Replace with your sender credentials.("email", "password")

program_start_date = date(2023, 12, 17)     #Replace with start date of your program.

# SENDING MMS
main_file_path = os.path.abspath("cat.jpg")             # Replace with media of choice in the current directory.
alt_file_path = os.path.abspath("cat-sleep.jpg")     # Replace with media to display on a rest day.
mime_maintype = "image"     # Replace with correct mime maintype of downloaded media.
mime_subtype = "jpeg"        # Replace with correct mime subtype of downloaded media.