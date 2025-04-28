from dotenv import load_dotenv
import os
import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.models.o_data_errors.o_data_error import ODataError

async def get_user_drive_id(client, user_id):
    try:
        drive = await client.users.by_user_id(user_id).drive.get()
        if drive and drive.id:
            print(f"Drive ID for user {user_id}: {drive.id}")
            return drive.id
        else:
            print(f"Could not retrieve drive ID for user {user_id}")
            return None
    except ODataError as e:
        print(f"Error getting drive: {e.error.message}")
        return None
    

async def get_drive_items(drive_id):
    tenant_id = os.getenv("TENANT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    scopes = ['https://graph.microsoft.com/.default']
    client = GraphServiceClient(credentials=credential, scopes=scopes)

    try:
        items = await client.drives.by_drive_id(drive_id).items.by_drive_item_id('root').children.get()
        if items and items.value:
            for item in items.value:
                print(f"ID: {item.id}, Name: {item.name}, Size: {item.size}, Folder: {item.folder}, File: {item.file}")
        else:
            print(f"No items found in the root of drive {drive_id}")
    except ODataError as e:
        print(f"Error getting drive items: {e.error.message}")


async def main():
    load_dotenv()

    client_id=os.getenv("CLIENT_ID")
    client_secret=os.getenv("CLIENT_SECRET")
    tenant_id=os.getenv("TENANT_ID")
    user_id=os.getenv("USER_ID")

    credentials = ClientSecretCredential(f'{tenant_id}',f'{client_id}',f'{client_secret}',)
    scopes = ['https://graph.microsoft.com/.default']
    client = GraphServiceClient(credentials=credentials, scopes=scopes)

    drive_id = await get_user_drive_id(client, user_id)

    if drive_id:
        await get_drive_items(drive_id)
    
if __name__ == "__main__":
    asyncio.run(main())