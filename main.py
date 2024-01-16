from sms import send_sms_by_email

def main():
    number = "6363179533"
    message = "Testing this script"
    provider = "AT&T"
    sender_credentials = ("eric.noharaleclair@gmail.com", "ujct wmrm kbjl pgun")
    send_sms_by_email(number, message, provider, sender_credentials)

if __name__ == "__main__":
    main()