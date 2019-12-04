from decouple import config

HOST = config('HOST')
PORTA = config('PORTA', cast=int)
