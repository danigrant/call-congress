import requests
import json
import scaleapi

republicans = []

# scaleapi
scaleapi_client = scaleapi.ScaleClient('00000')

# get all legislators from Sunlight Labs api
r = requests.get('https://congress.api.sunlightfoundation.com/legislators?per_page=all')

# check if each legislator is a republican.
# if they are republican, get their phone number

legislators = json.loads(r.text)['results']
for i in range (0,len(legislators)):
    if (legislators[i]['party'] == 'R'):
        # store the name and phone number
        republicans.append([legislators[i]['first_name'] + ' ' + legislators[i]['last_name'], str(legislators[i]['phone'])])

# for each name and phone number stored, make a call to scale api so they will call the legislator and say something
for i in range (0,len(republicans)):
    scaleapi_client.create_phonecall_task(
        callback_url='example.com', # change this
        instruction='Call this legislator and follow the script provided. If there is no answer, leave a voicemail.',
        phone_number= republicans[i][1],
        entity_name= republicans[i][0],
        script='', # add whatever you want to be said
    )
