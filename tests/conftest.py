import asyncio
import time
from socket import AF_INET, SHUT_RDWR, SOCK_STREAM, socket
from threading import Thread

import pytest

from app.settings import HOST, PORTA
from main import main


@pytest.fixture(scope='session')
def servidor():
    th_servidor = Thread(target=asyncio.run, args=(main(),))
    th_servidor.daemon = True
    th_servidor.start()
    time.sleep(0.001)
    yield (HOST, PORTA)


def _criar_cliente_socket():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(2)
    return sock


@pytest.fixture(scope='module')
def cliente_telnet1(servidor):
    sock = _criar_cliente_socket()
    sock.connect(servidor)
    yield sock
    sock.shutdown(SHUT_RDWR)
    sock.close()


@pytest.fixture
def cliente_telnet2(servidor):
    sock = _criar_cliente_socket()
    sock.connect(servidor)
    yield sock
    sock.shutdown(SHUT_RDWR)
    sock.close()
