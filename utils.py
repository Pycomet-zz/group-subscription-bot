from telethon.tl.functions.channels import EditBannedRequest
from config import *

channel = loop.run_until_complete(client.get_entity(int(GROUP)))

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"


def add_user(user_id: int):
    try:

        # Creating a single user invliteChat
        params = {"chat_id": GROUP, "user_id": user_id, "creates_join_request": True}

        req = requests.post(f"{BASE_URL}/createChatInviteLink", data=params).json()

        # Send the link to the new user
        url = req["result"]["invite_link"]
        loop.run_until_complete(
            client.send_message(
                user_id,
                f"""
        
        Hello Partner 😃,

        Here is your invite link to the Official Channel 
        {url}

        Welcome!
                """,
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

        params = {"chat_id": GROUP, "user_id": user_id}
        # Request to the oficial API banChatMemeber
        req = requests.post(f"{BASE_URL}/banChatMember", data=params).json()

        return True

    except Exception as e:
        logging.error(e)
        return False


def payment_status(id) -> bool:
    "Confirm payment session"

    response = stripe.checkout.Session.retrieve(id)
    status = response["payment_status"]

    if status == "unpaid":
        return False
    else:
        return True


def buy_plan():
    "Create Session & Return Url"

    result = stripe.checkout.Session.create(
        success_url=f"{SERVER_URL}/success",
        cancel_url=f"{SERVER_URL}/cancel",
        payment_method_types=["card"],
        line_items=[
            {
                "price": "plan_LPAfyb3ATk04wE",
                "quantity": 1,
            },
        ],
        mode="subscription",
    )

    return result["url"], result["id"]
