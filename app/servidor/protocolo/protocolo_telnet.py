from .protocolo_base import ProtocoloBase


class ProtocoloTelnet(ProtocoloBase):
    def __init__(self, reader, writer):
        """Protocolo de comunicação telnet."""
        super().__init__(reader, writer)

    async def receber_mensagens(self) -> str:
        """Recebe as mensagens do cliente."""
        mensagem = await self.reader.read(1024)
        mensagem = mensagem.decode()
        return mensagem.strip('\r\n')

    async def enviar_mensagens(self, mensagem: str) -> None:
        mensagem += '\n'
        self.writer.write(mensagem.encode())
        await self.writer.drain()
