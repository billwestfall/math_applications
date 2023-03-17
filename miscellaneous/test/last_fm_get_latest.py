import lastfm
import asyncio

client = lastfm.Client('client_key') # Replace with your client key (client_secret is optional)

async def main():
    recent_tracks = await client.get_recent_tracks("username", limit=5)
    print(recent_tracks[0].title) # prints the title of the users most recently scrobbled track

asyncio.run(main())
