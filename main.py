from definicionYalgoMas import dormir

# como el directorio tiene un archivo __init__.py entonces puedo importar desde ahí
# sería from [path_relativo].[archivo sin .py] import [clase o función]
from clases.tiempo import Contador

# ahora cuando ejecuto este archivo, lo que está en definicionYalgoMas.py NO se ejecuta
dormir()