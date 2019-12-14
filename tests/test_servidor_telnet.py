from unittest.mock import AsyncMock, call, Mock

import pytest

from app.telnet import conexoes, telnet


def criar_writer_mock() -> AsyncMock:
    """Cria e prepara um objeto writer mock para os testes."""
    writer_mock = AsyncMock()

    # Um objeto AsyncMock que não é chamado com await, faz com que apareça warning ao rodar os testes
    writer_mock.write = Mock()

    return writer_mock


@pytest.fixture
def writer_mock_interno() -> AsyncMock:
    """Cria um objeto que representa um cliente já conectado ao servidor."""
    writer_mock = criar_writer_mock()
    conexoes.append(writer_mock)
    yield writer_mock
    conexoes.remove(writer_mock)


@pytest.mark.asyncio
async def test_eco_da_mensagem():
    mensagens = [b'teste']
    calls = [call(b'teste\n')]

    writer_mock = criar_writer_mock()
    reader_mock = AsyncMock()
    reader_mock.read.side_effect = mensagens

    try:
        await telnet(reader_mock, writer_mock)
    except RuntimeError:
        pass

    writer_mock.write.assert_has_calls(calls)


@pytest.mark.asyncio
async def test_mensagem_para_todos_os_clientes(writer_mock_interno):
    mensagens = [b'teste']
    calls = [call(b'teste\n')]

    writer_mock = criar_writer_mock()
    reader_mock = AsyncMock()
    reader_mock.read.side_effect = mensagens

    try:
        await telnet(reader_mock, writer_mock)
    except RuntimeError:
        pass

    writer_mock_interno.write.assert_has_calls(calls)
