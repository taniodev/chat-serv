
class ProtocoloBase:
    def __init__(self, reader, writer):
        """Classe abstrata para a implementação de novos protocolos de comunicação."""
        self.reader = reader
        self.writer = writer

    async def receber_mensagens(self):
        """Receber mensagens do usuário."""
        raise NotImplementedError

    async def enviar_mensagens(self):
        """Enviar mensagens para o usuário."""
        raise NotImplementedError
