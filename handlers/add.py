from config import *
from utils import *

@bot.message_handler(commands=['adduser'])
def addUser(msg):
    """
    Add User And Schedule Removal Date
    """
    message = msg.text.split(" ")
    user = client.get_entity(int(message[1]))

    if user is not None:
        # Schedule User
        status = add_user(user.id)
        if status == True:
            bot.send_message(
                msg.from_user.id,
                "User Added Successfully"
            )
        else:
            bot.send_message(
                msg.from_user.id,
                "User Adding Failed"
            )

    else:
        bot.send_message(
            msg.from_user.id,
            "User Not Found"
        )

        