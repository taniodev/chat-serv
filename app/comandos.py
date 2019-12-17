from app.core.usuario import definir_nome


async def filtrar_comandos(usuario, mensagem: str):
    if not usuario.nome_id or not usuario.nome:
        await definir_nome(usuario, mensagem)
        return

    await usuario.msg.enviar_para_todos(f'{usuario.nome}: {mensagem}')
