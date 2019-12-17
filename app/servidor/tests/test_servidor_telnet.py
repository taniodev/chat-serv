from unittest.mock import AsyncMock, call, Mock

import pytest

from app.core import usuarios_conectados
from app.servidor.telnet import telnet


def criar_reader_mock(mensagens_do_cliente: list) -> AsyncMock:
    """Cria um objeto reader mock para os testes."""
    reader = AsyncMock()
    reader.read.side_effect = mensagens_do_cliente
    return reader


def criar_writer_mock() -> AsyncMock:
    """Cria e prepara um objeto writer mock para os testes."""
    writer_mock = AsyncMock()

    # Um objeto AsyncMock que não é chamado com await, faz com que apareça warning ao rodar os testes
    writer_mock.write = Mock()

    return writer_mock


async def rodar_telnet(reader_mock: AsyncMock, writer_mock: AsyncMock) -> None:
    try:
        await telnet(reader_mock, writer_mock)
    except StopAsyncIteration:
        pass


@pytest.fixture
def usuario_mock_interno() -> AsyncMock:
    """Cria um objeto que representa um cliente já conectado ao servidor."""
    usuario_mock = AsyncMock()
    usuarios_conectados['usr1'] = usuario_mock
    yield usuario_mock
    del usuarios_conectados['usr1']


@pytest.mark.asyncio
async def test_eco_da_mensagem():
    mensagens = [b'Fulano', b'teste']

    writer_mock = criar_writer_mock()
    reader_mock = criar_reader_mock(mensagens)
    await rodar_telnet(reader_mock, writer_mock)

    writer_mock.write.assert_called_with(b'Fulano: teste\n')


@pytest.mark.asyncio
async def test_mensagem_para_todos_os_clientes(usuario_mock_interno):
    mensagens = [b'Fulano', b'teste']

    writer_mock = criar_writer_mock()
    reader_mock = criar_reader_mock(mensagens)
    await rodar_telnet(reader_mock, writer_mock)

    usuario_mock_interno.msg.enviar.assert_called_with('Fulano: teste')


@pytest.mark.asyncio
async def test_mensagem_ao_conectar_no_servidor():
    mensagens = [b'Fulano']
    calls = [
        call('> Digite o seu nome:\n'.encode()),
        call('*. Fulano entra na conversação\n'.encode()),
    ]

    writer_mock = criar_writer_mock()
    reader_mock = criar_reader_mock(mensagens)
    await rodar_telnet(reader_mock, writer_mock)

    writer_mock.write.assert_has_calls(calls)
