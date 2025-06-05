# mercado200
Desarrollado por SERGIO EMILIANO LOPEZ BAUTISTA [25 04 2025] 
Colaboración con:

NOTA IMPORTANTE:En caso de hacer una modificación, colocarla en una nueva rama. 
Si se logra una nueva versión estable, coloca tu nombre en el apartado de COLABORACIÓN y notificalo en este README.md con los cambios agregados respecto a la versión anterior.

= V.2.0.0 = 
    Versión beta 
Un sólo agente realiza un trabajo general de investigación con un prompt no optimizado colocado directamente como un f-string

= V.2.0.3 =
    Prototipo de interfaz
Los pequeños cambios agregados a esta versión involucran:
    - Instrucciones cortas para introducir al usuario al funcionamiento general de la herramienta
    - La animación de maquina de escribir al despliegue de la vista previa de la información
    - Validación a la entrada de datos
*Esta versión no se incluyó en un commit*

= V.2.1.3 =
    Estructuración general del proyecto
Como proposito genreal, se estructuró el proyecto con dos subcarpetas con el objetivo de que se haga uso de archivos externos para poder leer, modificar y usar prompts optimizados con el uso de prompt engineering y la estructura de prompt propuesta por OpenAI.
La estructra de subcarpetas y archivos propuesta en esta versión es:

mercado200/
|
+-- mercado200.py
+-- requeriments.txt
+-- LICENSE
+-- README.md
|
+-- data/
|   |
|   +-- instrucciones.txt
|   +-- plantilla00_OpenAI.txt
|   ...
|   +-- plantilla??_OpenAI.txt
|
+-- utils/
    |
    +-- prompts.py

NOTA: La estructura y funcionamiento serán ampliadas en la documentación anexa a las carpetas en  proximas versiones.

= V.2.2.3 =
    Barra lateral
Al diseño de la intefaz del usuario se le hizo un cambio sutil, pero importante al colocar las instrucciones, la caja de entrada de texto y el botón para guardar la información en una barra lateral desplegable, con la finalidad de que sea más cómo visualmente al usuario el despliegue de la información