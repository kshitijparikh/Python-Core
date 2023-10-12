import asyncio
import websockets
import keyboard

#Start the client
async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        done=False
        while not done:
            if keyboard.is_pressed('space'):
                await websocket.send('buzz')
                message=await websocket.recv()
                print(message)
                done=True

#Run the client
asyncio.run(start_client())