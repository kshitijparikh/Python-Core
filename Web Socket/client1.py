import asyncio 
import websockets

async def hello():
    url="ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name=input('Whats your name?')
        
        await websocket.send(name)
        print(f"Client send: {name}")
        
        greeting=await websocket.recv()
        print(f"Client received: {greeting}")
        
if __name__=='__main__':
    asyncio.run(hello())