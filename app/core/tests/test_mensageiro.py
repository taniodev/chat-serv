from unittest.mock import AsyncMock, Mock

import pytest

from app.core.mensageiro import Mensageiro


@pytest.mark.asyncio
async def test_metodo_enviar(mocker):
    usuario_mock = AsyncMock()
    mensageiro = Mensageiro({}, usuario_mock)
    await mensageiro.enviar('teste')
    usuario_mock.protocolo.enviar_mensagens.assert_called_once_with('teste')


@pytest.mark.asyncio
async def test_enviar_para_todos(mocker):
    usuarios_conectados = {'usr1': AsyncMock(), 'usr2': AsyncMock()}

    mensageiro = Mensageiro(usuarios_conectados, Mock())
    await mensageiro.enviar_para_todos('teste')

    usuarios_conectados['usr1'].msg.enviar.assert_called_once_with('teste')
    usuarios_conectados['usr2'].msg.enviar.assert_called_once_with('teste')
