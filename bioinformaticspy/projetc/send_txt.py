from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC59b7fd92f411b7f93aa3712588d39e2e"
auth_token  = "fce87adf400e5f625e8043d8361eebb7"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="momo momo mmooo hhhhhhhhh",
    to="+33648768525",    # Replace with your phone number
    from_="+33977552058") # Replace with your Twilio number
print message.sid