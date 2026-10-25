# Dentro del texto — Fusion para DaVinci Resolve

Un efecto reutilizable de Paco Estrada: el vídeo se ve dentro de las letras sobre fondo negro. El texto crece hasta dar paso a la escena completa, mientras el vídeo conserva su tamaño.

Probado por el autor en **DaVinci Resolve Studio 21 sobre Linux**. No requiere complementos adicionales. Otras versiones y sistemas no se han probado.

## Ejemplo del efecto

![Vídeo dentro de las letras de LINUX](https://github.com/user-attachments/assets/79fccbc1-6435-44b3-852f-2fba9f36ee09)

[Ver o descargar el vídeo de ejemplo](demo.mp4)

## Descargar e instalar

1. Descarga [Paco-Dentro-del-texto.drfx](Paco-Dentro-del-texto.drfx?raw=true).
2. Haz doble clic y acepta instalarlo en Resolve. Si tu sistema no lo abre, arrastra el archivo a la página **Fusion**.
3. Reinicia Resolve si el efecto no aparece.
4. En **Biblioteca de efectos → Efectos → Fusion Effects**, busca **Paco - Dentro del texto**, en la carpeta Paco.

Es un **efecto aplicado al clip**, no un título para colocar en una pista vacía.

## Uso

1. Arrastra el efecto sobre un clip de vídeo. Para la primera prueba, usa uno de al menos seis segundos.
2. Selecciona el clip y abre **Inspector → Efectos**.
3. Escribe una palabra corta y elige una tipografía gruesa. La fuente inicial es **DejaVu Sans Bold**; puedes sustituirla si no está instalada.
4. Reproduce desde el principio del clip.

| Control | Función | Valor inicial |
| --- | --- | --- |
| Texto, Fuente, Estilo | Contenido y tipografía | ENTRA / DejaVu Sans / Bold |
| Tamano inicial | Tamaño del texto antes del acercamiento | 0,18 |
| Espera (fotogramas) | Tiempo de lectura antes del zoom | 25 |
| Zoom (fotogramas) | Duración del acercamiento | 75 |
| Ampliacion final | Factor de ampliación de las letras | 60 |
| Entrada X / Entrada Y | Punto hacia el que se dirige el acercamiento | 0,5 / 0,5 |

A **25 fps**, los valores iniciales equivalen a un segundo de espera y tres de zoom. A **30 fps**, usa 30 y 90; a **60 fps**, 60 y 180. La suma de espera y zoom debe caber en el clip. Los tiempos no se adaptan automáticamente al recortarlo.

Para atravesar una letra, coloca el cabezal a mitad del acercamiento y ajusta **Entrada X/Y** en pequeños pasos hasta entrar en un trazo sólido. El punto no se detecta automáticamente. El último 15 % del zoom desvanece el negro restante para terminar con la escena completa, incluso si quedan huecos entre letras.

## Instalación manual en Linux

Como alternativa al DRFX, copia [Paco-Dentro-del-texto.setting](Paco-Dentro-del-texto.setting) en:

```text
~/.local/share/DaVinciResolve/Fusion/Templates/Edit/Effects/Paco/
```

Crea las carpetas si faltan. Utiliza un solo método de instalación para evitar duplicados.

## Desarrollo

El archivo `.setting` es el código editable de Fusion. El `.drfx` es un ZIP que contiene ese archivo en `Edit/Effects/Paco/Paco - Dentro del texto.setting`.

Para generar el instalador desde el código, ejecuta `python3 build.py`. Solo utiliza la biblioteca estándar de Python.

Esta versión incluye la corrección del identificador del nodo de controles (`Custom`). Si conservas una versión inicial que muestra «Unknown tool found: CustomTool», retira ese paquete antiguo de la carpeta de plantillas con Resolve cerrado.

## Autor y licencia

Paco Estrada. Código y plantilla bajo licencia MIT, como los otros títulos Fusion del autor. El vídeo se incluye como demostración; no queda cubierto por la licencia del código.
