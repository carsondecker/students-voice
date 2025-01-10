import asyncio

message_count = 0

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    try:
        while True:
            data = await reader.read(100)
            message = data.decode()

            print(data)
            
            if not data:
                break
            
            message = data.decode()
            print(f"Received {message!r} from {addr!r}")
            global message_count
            message_count += 1  
            print(f"Messages Received: {message_count}")
            print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
    finally:
        print("Close the connection")
        writer.close()
        await writer.wait_closed()

async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    
    addr = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addr}')
    
    async with server:
        await server.serve_forever()
    
async def main():
    server_task = asyncio.create_task(run_server())
    
    await asyncio.gather(server_task)

asyncio.run(main())