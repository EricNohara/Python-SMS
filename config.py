from datetime import date

number = "6363179533"   # Replace with your phone number.
provider = "AT&T"       # Replace with correct phone provider, match with keys in dictionary provided in providers.py file.
sender_credentials = ("eric.noharaleclair@gmail.com", "ujct wmrm kbjl pgun")       # Replace with your sender credentials.("email", "password")

program_start_date = date(2023, 12, 18)     #Replace with start date of your program.

# SENDING MMS
file_path = "cat.jpg"       # Replace with media of choice in the current directory.
mime_maintype = "image"     # Replace with correct mime maintype of downloaded media.
mime_subtype = "jpg"        # Replace with correct mime subtype of downloaded media.