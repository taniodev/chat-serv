
class Mensageiro:
    def __init__(self, usuarios_conectados: dict, usuario):
        self._usuarios_conectados = usuarios_conectados
        self._usuario = usuario

    async def enviar(self, mensagem: str) -> None:
        """Envia a mensagem para o objeto da conexão atual."""
        await self._usuario.protocolo.enviar_mensagens(mensagem)

    async def enviar_para_todos(self, mensagem: str) -> None:
        """Envia mensagem para todas as conexões."""
        for _, usuario in self._usuarios_conectados.items():
            await usuario.msg.enviar(mensagem)
