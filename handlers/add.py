from config import *


@bot.message_handler(commands=['adduser'])
def addUser(msg):
    """
    Add User Against Scheduled Date
    """
    message = msg.text.split(" ")
    user = client.get_entity(int(message[1]))

    if user is not None:
        # Schedule User
        

    else:
        bot.send_message(
            msg.from_user.id,
            "User Not Found"
        )