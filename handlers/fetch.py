from config import *

administrators = []


@bot.message_handler(commands=["fetchusers"])
def fetcher(msg):
    user = User(id=msg.from_user.id)

    pull_subscribers(user)


def pull_subscribers(user):

    # group = bot.get_chat(GROUP)
    # group.wait()

    global administrators

    # [administrators.append(admin.user.id) for admin in bot.get_chat_administrators(GROUP)]

    # Get group entity and members
    channel = loop.run_until_complete(client.get_entity(int(GROUP)))

    # members = loop.run_until_complete(client.get_participants(channel, aggressive=True))
    members = loop.run_until_complete(client.get_participants(channel))

    numberOfMembers = len(members)

    bot.send_message(user.id, f"{numberOfMembers} Subscribers found in {channel.title}")

    # Writing to excel file
    export(members)

    administrators = []

    file = open("Users.csv", "rb")
    bot.send_document(user.id, caption="Extraction Complete!!", data=file)


def export(members):
    """
    Write to Users.csv
    """
    # Sorting the members by date
    data = []
    # Input scraped content
    for user in members:
        if user.bot == False:
            if user.id not in administrators:

                try:
                    joined_date = user.participant.date
                    join = date.today() - joined_date.date()
                    joined = join.days
                except Exception as e:
                    joined = "0"

                data.append(
                    {
                        "First Name": user.first_name,
                        "Last Name": user.last_name,
                        "Username": user.username,
                        "User Id": int(user.id),
                        "Joined Days Count": int(joined),
                    }
                )
    data.sort(key=lambda x: x["Joined Days Count"], reverse=True)

    # Open csv file
    with open("Users.csv", "w", encoding="utf8") as file:

        # Input headers
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # write headers for columns
        [writer.writerow(user) for user in data]
