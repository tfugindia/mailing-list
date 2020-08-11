import requests
API_KEY = "" #API Key (https://app.mailgun.com/app/account/security/api_keys)

def send_simple_message(to,subject,template):
    '''This function will send the emails to attendees.'''
    return requests.post(
        "https://api.mailgun.net/v3/mail.tfug.in/messages",
        auth=("api", API_KEY),
		data={"from": "TFUG India <postmaster@mail.tfug.in>",
			"to": to,
			"subject": subject,
			"template": template,
			"h:X-Mailgun-Variables": "{\"test\": \"test\"}"})

to = "" # mailing list Alias address (https://app.mailgun.com/app/sending/lists)
subject = "" # mail subject
template = "" #template name (https://app.mailgun.com/app/sending/domains/mail.tfug.in/templates)

# send_simple_message(to,subject,template)	
