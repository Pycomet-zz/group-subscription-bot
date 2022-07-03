from config import *
from utils import *


@bot.message_handler(commands=["adduser"])
def addUser(msg):
    """
    Add User And Schedule Removal Date
    """
    message = msg.text.split(" ")

    user = loop.run_until_complete(client.get_entity(message[1]))

    if user is not None:
        # Schedule User
        status = add_user(msg.from_user.id)
        if status == True:
            bot.send_message(
                msg.from_user.id, ts.translate("User Invited Successfully", "es")
            )
        else:
            bot.send_message(msg.from_user.id, ts.translate("User Adding Failed", "es"))

    else:
        bot.send_message(msg.from_user.id, ts.translate("User Not Found", "es"))
