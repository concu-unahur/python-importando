import time
import logging

# la voy a querer importar
def dormir():
    logging.info('Ejecutando dormir()')
    time.sleep(1)


# entonces para que esto no se ejecute cuando importan dormir()
# hago así

if __name__ == '__main__':
    logging.info('Ahora esto no se ejecuta cuando corro main.py')

# pueden probar de comentar el if (e identar bien la siguiente línea)
# y volver a correr main.py, como para ver la diferencia