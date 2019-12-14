from unittest.mock import AsyncMock

import pytest

from app.mensageiro import Mensageiro


@pytest.mark.asyncio
async def test__mensagem():
    destinatario = AsyncMock()
    mensageiro = Mensageiro([])
    await mensageiro._mensagem(destinatario, 'teste')
    destinatario.write.assert_called_once_with(b'teste\n')
    destinatario.drain.assert_called


@pytest.mark.asyncio
async def test_enviar_para_todos(mocker):
    conexoes = [AsyncMock(), AsyncMock()]
    _mensagem_mock = mocker.patch('app.mensageiro.Mensageiro._mensagem')

    mensageiro = Mensageiro(conexoes)
    await mensageiro.enviar_para_todos('teste')

    assert _mensagem_mock.call_count == len(conexoes)
