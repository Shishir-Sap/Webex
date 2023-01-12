import json
import requests
from webexteamssdk import WebexTeamsAPI

# Access roken valid for 12 hours: https://developer.webex.com/docs/api/getting-started ### (login required)

# get your own token
current_access_token = "Y2FlNGE2MGEtY2FiYS00NTJkLTk5OGMtYjgyMGU1YmEyOWRhM2MzYjY4MWMtOWFh_P0A1_f385d8b4-839f-42c4-9819-c9b577f54c40"

access_token = current_access_token
# set room url
room_url = 'https://api.ciscospark.com/v1/rooms'


# Set the headers for the API call
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}


# Read the JSON file into a Python dictionary
with open('data.json') as json_file:
    json_string_data = json_file.read()
    json_data = json.loads(json_string_data)

    print((json_data.keys()))
    for group in json_data.keys():
        print(group)
        # create_group

        payload_space = {"title": group}
        res_space = requests.post(
            room_url, headers=headers, json=payload_space)
        NEW_SPACE_ID = res_space.json()["id"]
        for xmbr in json_data[group]:
            # print(x)
            print(xmbr["name"])
            print(xmbr["email"])
            # create member
            room_id = NEW_SPACE_ID
            person_email = xmbr["email"]
            url2 = 'https://api.ciscospark.com/v1/memberships'
            payload_member = {'roomId': room_id, 'personEmail': person_email}
            res_member = requests.post(
                url2, headers=headers, json=payload_member)
