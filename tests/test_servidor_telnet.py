
def test_eco_da_mensagem(cliente_telnet1):
    cliente_telnet1.send(b'testando')
    assert b'testando' in cliente_telnet1.recv(1024)


def test_mensagem_para_todos_os_clientes(cliente_telnet1, cliente_telnet2):
    cliente_telnet1.send(b'testando')
    assert b'testando' in cliente_telnet2.recv(1024)
