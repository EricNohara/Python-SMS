from sms import send_sms_by_email
from mms import send_mms_by_email
from getsheetdata import FormatSheet
from datetime import date

def main():
    # number = "3149396381"
    number = "6363179533"
    format_sheet = FormatSheet(date(2023, 12, 18))
    message = format_sheet.format_sms_msg()
    print(message)
    provider = "AT&T"
    sender_credentials = ("eric.noharaleclair@gmail.com", "ujct wmrm kbjl pgun")
    # send_sms_by_email(number, message, provider, sender_credentials)

    # SENDING MMS
    file_path = "cat.jpg"
    mime_maintype = "image"
    mime_subtype = "jpg"

    send_mms_by_email(number, message, file_path, mime_maintype, mime_subtype, provider, sender_credentials)

if __name__ == "__main__":
    main()