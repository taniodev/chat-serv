
def test_servidor_de_eco(cliente):
    cliente.send(b'testando')
    assert b'testando' in cliente.recv(1024)
