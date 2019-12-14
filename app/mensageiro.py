
class Mensageiro:
    def __init__(self, conexoes):
        self._conexoes = conexoes

    async def _mensagem(self, destinatario, mensagem: str) -> None:
        """Enviar mensagem."""
        mensagem += '\n'
        destinatario.write(mensagem.encode())
        await destinatario.drain()

    async def enviar_para_todos(self, mensagem: str) -> None:
        """Envia mensagem para todas as conexões."""
        for conexao in self._conexoes:
            await self._mensagem(conexao, mensagem)
