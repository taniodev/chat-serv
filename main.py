import asyncio

from app.telnet import telnet
from app.settings import HOST, PORTA


async def main():
    servidor = await asyncio.start_server(telnet, HOST, PORTA)

    async with servidor:
        await servidor.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

    print('Servidor finalizado')
