from .protocolo_base import ProtocoloBase


class ProtocoloTelnet(ProtocoloBase):
    """Protocolo de comunicação telnet."""

    def __init__(self, reader, writer):
        super().__init__(reader, writer)

    async def receber_mensagens(self) -> tuple:
        esta_conectado = True
        mensagem = await self.reader.read(1024)
        mensagem = mensagem.decode(encoding='iso-8859-1')

        # Quando a conexão é perdida, o socket recebe ifinitas mensagens b''.
        if mensagem == '':
            esta_conectado = False

        return (self._filtrar(mensagem), esta_conectado)

    async def enviar_mensagens(self, mensagem: str) -> None:
        mensagem += '\n'
        self.writer.write(mensagem.encode(encoding='iso-8859-1'))
        await self.writer.drain()
