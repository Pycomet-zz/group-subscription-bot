from config import *

administrators = []

@bot.message_handler(commands=['fetchusers'])
def fetcher(msg):
    user = User(id = msg.from_user.id)

    pull_subscribers(user)



def pull_subscribers(user):

    # group = bot.get_chat(GROUP)
    # group.wait()

    global administrators

    # [administrators.append(admin.user.id) for admin in bot.get_chat_administrators(GROUP)]

    # Get group entity and members
    channel = loop.run_until_complete(
        client.get_entity(int(GROUP))
    )
 
    members = loop.run_until_complete(client.get_participants(channel, aggressive=True))
    
    numberOfMembers = len(members)

    bot.send_message(user.id, f"{numberOfMembers} Subscribers found in {channel.title}")

    # Writing to excel file
    export(members)

    administrators = []

    file = open("Users.csv", 'rb')
    bot.send_document(user.id, caption="Extraction Complete!!", data=file)


def export(members):
    """
    Write to Users.csv
    """

    #Open csv file
    with open("Users.csv", "w", encoding="utf8") as file:

        #Input headers
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() # write headers for columns

        #Input scraped content
        for user in members:
            if user.bot == False:
                if user.id not in administrators:

                    if str(user.status) == "UserStatusRecently()":
                        status = "Last Seen Not Long Ago"
                    elif str(user.status) == "UserStatusLastWeek()":
                        status = "Last Seen Last Week"
                    elif str(user.status) == "UserStatusLastMonth()":
                        status = "Last Seen Last Month"
                    else:
                        status = "Not Active For A While"

                    writer.writerow({
                        'First Name': user.first_name,
                        'Last Name': user.last_name,
                        'Username': user.username,
                        'Id': int(user.id),
                        'User Status': status
                    })