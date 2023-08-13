from telethon import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

client = TelegramClient('anon', API_ID, API_HASH)


async def main():
    dialogs = await client.get_dialogs()

    group_title = input('Write group title\n    >>: ')
    message = input('Write message\n    >>: ')

    target_group = None
    for dialog in dialogs:
        if dialog.title == group_title:
            target_group = dialog
            break

    group_entity = target_group.entity
    all_participants = await client.get_participants(group_entity, aggressive=True)

    for participans in all_participants:
        await client.send_message(participans.id, message)

with client:
    client.loop.run_until_complete(main())
