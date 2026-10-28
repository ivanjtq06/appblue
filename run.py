
import sys
import os

# Obtiene la ruta absoluta de la carpeta donde está run.py (C:\appblue)
project_root = os.path.dirname(os.path.abspath(__file__))
# La inserta al inicio de las rutas de búsqueda de Python
sys.path.insert(0, project_root)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)