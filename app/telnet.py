
async def telnet(reader, writer):
    data = await reader.read(1024)

    writer.write(data)
    await writer.drain()

    writer.close()
