
conexoes = []


async def telnet(reader, writer):
    conexoes.append(writer)

    while True:
        data = await reader.read(1024)

        if 'sair' in data.decode():
            break

        for conexao in conexoes:
            conexao.write(data)
            await conexao.drain()

    conexoes.remove(writer)
    writer.close()
