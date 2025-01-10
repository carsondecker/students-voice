import asyncio

async def connect_and_send():
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 8888)
        while True:
            msg = input("Type the message to send to the server: ")
            print(f'Send: {msg!r}')
            writer.write(msg.encode())
            await writer.drain()

            data = await reader.read(100)
            print(f'Received: {data.decode()!r}')

asyncio.run(connect_and_send())