from sms import send_sms_by_email
from mms import send_mms_by_email
from getsheetdata import FormatSheet
from config import *

def main():
    """Do send the message containing the user's workout for today to the user's phone via a text with an image."""
    format_sheet = FormatSheet(program_start_date)
    message = format_sheet.format_sms_msg()
    print(message)
    # Uncomment to send the message as an SMS without an image.
    # send_sms_by_email(number, message, provider, sender_credentials)

    if message == "Today is a rest day.":
        send_mms_by_email(number, message, alt_file_path, mime_maintype, mime_subtype, provider, sender_credentials)
    else:
        send_mms_by_email(number, message, main_file_path, mime_maintype, mime_subtype, provider, sender_credentials)

if __name__ == "__main__":
    main()