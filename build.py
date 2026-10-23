"""Empaqueta el código editable en un instalador de Fusion."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
source = root / "Paco-Dentro-del-texto.setting"
destination = root / "Paco-Dentro-del-texto.drfx"
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    archive.write(source, "Edit/Effects/Paco/Paco - Dentro del texto.setting")
print(destination)
