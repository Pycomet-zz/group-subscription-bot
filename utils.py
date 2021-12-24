from telethon.tl.functions.channels import EditBannedRequest
from config import *



def add_user(user_id:int):
    # Get group entity and members
    channel = loop.run_until_complete(
        client.get_entity(int(GROUP))
    )
 
    try:
        loop.run_until_complete(
            client(
                InviteToChannelRequest(
                    channel,
                    [user_id]
                )
            )
        )
        return True

    except Exception as e:
        return False
    





def remove_user(user_id):
    # channel = loop.run_until_complete(
    #     client.get_input_entity(int(GROUP))
    # )
# client.invoke(EditBannedRequest(channel_entity, client.get_input_entity('username'), ChannelBannedRights(datetime.datetime(2020, 12, 25), view_messages=True, send_messages=True,send_media=True,send_stickers=True,send_gifs=True,send_games=True, send_inline=True, embed_links=True)))

    try:
        loop.run_until_complete(
            client(
                DeleteChatUserRequest(
                    int(GROUP),
                    user_id,
                    revoke_history=True
                )
            )
        )
        return True
    except Exception as e:
        return False
