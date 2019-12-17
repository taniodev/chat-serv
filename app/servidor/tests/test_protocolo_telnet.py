from unittest.mock import AsyncMock, Mock

import pytest

from app.servidor.protocolo import ProtocoloTelnet


@pytest.mark.asyncio
async def test_receber_mensagens():
    reader_mock = AsyncMock()
    reader_mock.read.return_value = b'teste'
    writer_mock = AsyncMock()
    protocolo = ProtocoloTelnet(reader_mock, writer_mock)

    mensagem = await protocolo.receber_mensagens()

    assert mensagem == 'teste'


@pytest.mark.asyncio
async def test_enviar_mensagens():
    writer_mock = AsyncMock()
    writer_mock.write = Mock()
    reader_mock = AsyncMock()
    protocolo = ProtocoloTelnet(reader_mock, writer_mock)

    await protocolo.enviar_mensagens('teste')

    writer_mock.write.assert_called_once_with(b'teste\n')
    writer_mock.drain.assert_called
