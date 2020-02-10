from .protocolo_base import ProtocoloBase


class ProtocoloTelnet(ProtocoloBase):
    """Protocolo de comunicação telnet."""

    def __init__(self, reader, writer):
        super().__init__(reader, writer)

    async def receber_mensagens(self) -> str:
        mensagem = await self.reader.read(1024)
        mensagem = mensagem.decode(encoding='iso-8859-1')
        return self._filtrar(mensagem)

    async def enviar_mensagens(self, mensagem: str) -> None:
        mensagem += '\n'
        self.writer.write(mensagem.encode(encoding='iso-8859-1'))
        await self.writer.drain()
