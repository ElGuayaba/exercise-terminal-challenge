# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
from pathlib import Path
import os
import pandas as pd

files = [str(file) for file in Path(".").rglob("")]

temp = str(files[0])

result = [
    {
        'path': filePath, 
        'size': os.path.getsize(filePath), 
        'lastmod': os.path.getmtime(filePath)
        } for filePath in files]

df = pd.DataFrame(result)

df.to_csv('result.csv')

# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV