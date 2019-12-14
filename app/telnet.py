
from app.mensageiro import Mensageiro

conexoes = []


async def telnet(reader, writer):
    conexoes.append(writer)
    msg = Mensageiro(conexoes)

    while True:
        data = await reader.read(1024)
        data = data.decode()

        if 'sair' in data:
            break

        await msg.enviar_para_todos(data)

    conexoes.remove(writer)
    writer.close()
