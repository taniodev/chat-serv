
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

    async def receber_mensagens(self) -> tuple:
        """
        Receba as mensagens do socket.

        :return: tuple(
            <str: A mensagem que veio do socket>,
            <bool: Se for False, indica que a conexão foi interrompida e o loop principal será encerrado>,
        )
        A conexão pode ser interrompida quando o usuário fecha a janela do cliente que está usando para se conectar.

        """
        raise NotImplementedError

    async def enviar_mensagens(self, mensagem: str) -> None:
        """Envie uma mensagem para o socket."""
        raise NotImplementedError
