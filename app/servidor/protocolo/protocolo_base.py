
class ProtocoloBase:
    """Classe abstrata para a implementação de novos protocolos de comunicação."""

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def _filtrar(self, mensagem: str) -> str:
        """
        Aplique um filtro à mensagem.

        Remove espaços no início e no fim da string.

        :param mensagem: Uma string que será filtrada.
        :return: A string tratada.

        """
        mensagem = mensagem.strip()
        return mensagem

    async def receber_mensagens(self) -> str:
        """Receba as mensagens do socket."""
        raise NotImplementedError

    async def enviar_mensagens(self, mensagem: str) -> None:
        """Envie uma mensagem para o socket."""
        raise NotImplementedError
