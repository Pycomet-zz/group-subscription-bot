from telethon.tl.functions.channels import EditBannedRequest
from config import *

channel = loop.run_until_complete(
    client.get_entity(int(GROUP))
)

BASE_URL = F'https://api.telegram.org/bot{TOKEN}'

def add_user(user_id:int):
    try:

        # Creating a single user invliteChat
        params= {
            'chat_id': GROUP,
            'user_id': user_id,
            'creates_join_request': True
        }

        req = requests.post(f'{BASE_URL}/createChatInviteLink', data=params).json()

        # Send the link to the new user
        url = req['result']['invite_link']
        loop.run_until_complete(
            client.send_message(
                user_id,
                f"""
        
        Hello Partner 😃,

        Here is your invite link to the Official Channel 
        {url}

        Welcome!
                """
            )
        )


        # set date of removal (APScheduler)

        return True

    except Exception as e:
        logging.error(e)
        return False
    





def remove_user(user_id):
    "Removes User From The Channel"
    try:

        params= {
            'chat_id': GROUP,
            'user_id': user_id
        }
        # Request to the oficial API banChatMemeber
        req = requests.post(f'{BASE_URL}/banChatMember', data=params).json()

        return True

    except Exception as e:
        logging.error(e)
        return False
