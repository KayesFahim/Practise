from twilio.rest import Client

account_sid = 'AC2666b74bfdf2bab0db93db52046a1817'
auth_token = 'f03a3ff9cae14940baf4af36e35eb4c6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hiii, Ruten Howadar. You Win 500000Taka From NSU. Visit Accounts and collect your money",
                     from_='+12089043232',
                     to='+8801766820662'
                 )

print(message.sid)