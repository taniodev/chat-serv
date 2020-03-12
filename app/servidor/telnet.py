from app.core.comandos import filtrar_comandos
from app.core.usuario import Usuario
from app.servidor.protocolo import ProtocoloTelnet


async def telnet(reader, writer):

    protocolo = ProtocoloTelnet(reader, writer)
    usr = Usuario(protocolo)
    await usr.msg.enviar('> Digite o seu nome:')

    while usr.esta_conectado:
        data, usr.esta_conectado = await usr.protocolo.receber_mensagens()

        if not data:
            continue

        await filtrar_comandos(usr, data)

    await usr.desconectou()
    writer.close()
    await writer.wait_closed()
