'''
    TEMA 78

    ---------Crear Ejecutables de nuestros progrmas-----------

    1º - Instalar el modulo pyinstaller en la consola de Windows: 
        - Escribir: pip install pyinstaller

    2º - En la consola de Windows nos vamos al directorio donde temenos el archivo para convertir a .exe
        - Escribir: pyinstaller nombreDelarchivo.py

    3º - Para que no salga la consola de fondo debemos escribirlo con las siguente extensión.
        - Escribir: pyinstaller --windowed nombreDelarchivo.py

    4º - Si el archivo ".exe" queremos que se trate de un solo archivo sin que nos cree las carpetas añadidas.
        de modo que funcione en todos los ordenadores y sin que necesite python instalado.
        - Escribir: pyinstaller --windowed --onefile nombreDelarchivo.py

    5º - Finalmente para añadir un icono al archivo ".exe"
        - Escribir: pyinstaller --windowed --onefile --ico=./nombreArchivo.ico
'''