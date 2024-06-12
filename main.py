import asyncio
import websockets
import json

async def send_position_and_color(websocket, path):
    position = 0
    while True:
        color = {"r": 1, "g": 0, "b": 0} if position % 2 == 0 else {"r": 0, "g": 1, "b": 0}
        coordinates = {"x": position, "y": position * 0.5, "z": position * 0.25}
        message = json.dumps({"coordinates": coordinates, "color": color})
        await websocket.send(message)
        await asyncio.sleep(1)
        position += 1

start_server = websockets.serve(send_position_and_color, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server started at ws://localhost:8765")
asyncio.get_event_loop().run_forever()
