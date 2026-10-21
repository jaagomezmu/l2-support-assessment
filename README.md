# Prueba L2 — C05 — 30 minutos

## Ticket

El archivo diario de `cliente-885`, ejecución `RUN-C05-2800`, no llegó a su destino.
El contenedor figura activo. Investiga el incidente, corrige la configuración
y demuestra la entrega en este laboratorio. Hay mensajes históricos y de otros servicios.

Docker es real; AWS está **simulado**. No hay cuenta, credenciales ni servicios AWS reales.
No es necesario escribir Python. Todos los datos son ficticios.

## Inicio

Después de clonar `caso/C05`, crea `entrega/C05` y ejecuta:

```sh
python3 tools/lab.py start
```

Las imágenes están precargadas. Si el entorno no inicia, avisa al entrevistador.
Consulta [la referencia](docs/REFERENCIA.md) y `case/CONTRATO.md`.

## Trabajo y tiempos

- 0–4: clonar, crear rama e iniciar.
- 4–12: investigar y completar el diagnóstico; crear el primer commit.
- 12–20: corregir `config.env` y aplicar la configuración.
- 20–24: comprobar el resultado y documentarlo.
- 24–27: segundo commit, push y entrega del SHA.
- 27–30: explicar evidencia y resultado al entrevistador.

Puedes pedir ayuda; se registrará la orientación proporcionada. Se permiten
documentación, Google y chats de IA. No agentes ni IA en la terminal. Indica
brevemente el uso de IA en la plantilla; no se penaliza su uso permitido.

## Preguntas

Responde en `RESPUESTAS.json` usando el identificador de opción, evidencia,
justificación y un comando utilizado. Para P2–P4 cita datos de tu caso, no solo
el nombre de un error. Para P1 relaciona estado del contenedor y resultado de aplicación.

### P1. ¿Qué demuestra que el contenedor figure en ejecución?

- `permisos_completos` — Tiene todos los permisos necesarios
- `entrega_confirmada` — El archivo llegó al destino
- `sin_errores` — No hubo errores de aplicación
- `proceso_activo` — Su proceso principal sigue activo
### P2. ¿Qué explica el fallo de la entrega del ticket?

- `destino_fuera_alcance` — El destino utilizado está fuera del alcance autorizado
- `contenedor_detenido` — El contenedor está detenido
- `timeout_actual` — La ejecución actual agotó el tiempo de red
- `entrada_ausente` — No existe el archivo de entrada
### P3. ¿Qué evento corresponde al incidente del ticket?

- `RUN-C05-2800` — PUT_OBJECT / AccessDenied de RUN-C05-2800
- `OTHER-C05-530` — DELIVERED de OTHER-C05-530
- `METRICS-C05` — WARN_BUFFER_HIGH de METRICS-C05
- `OLD-C05-188` — NETWORK_TIMEOUT de OLD-C05-188
### P4. ¿Qué acción respaldan el procedimiento y la evidencia?

- `corregir_destino` — Corregir el destino configurado y validar la entrega
- `ampliar_permisos` — Autorizar escritura sobre todos los objetos
- `reiniciar_todo` — Reiniciar todos los servicios sin revisar el rechazo
- `reintentar_igual` — Reintentar sin cambiar ni revisar la configuración

## Entrega

1. Guarda evidencia inicial con `python3 tools/lab.py capture` y crea un commit
   de diagnóstico antes de corregir la configuración.
2. Modifica únicamente `config.env`, `RESPUESTAS.json` y archivos bajo `evidence/`.
   Conserva la aplicación, política, contrato y datos originales.
3. Comprueba el resultado con `python3 tools/lab.py check`; ejecuta `capture`
   nuevamente para guardar el recibo final. El recibo inicial se conserva.
4. Completa el resumen (hasta seis líneas), la validación y el uso de IA.
5. Ejecuta `python3 tools/lab.py answers`, revisa el diff y crea el segundo commit.
6. Publica `entrega/C05` y entrega el SHA, comprobando la referencia remota.

No se pide pull request. Puedes usar comandos equivalentes a la referencia.
Las comprobaciones públicas ayudan a validar; no asignan la nota final.
Un commit local no equivale a un push. Nunca incluyas datos reales o secretos.

## Evaluación

Investigación 25%, Docker 20%, conceptos AWS 20%, corrección/validación 15%,
Git 10%, comunicación 10%. Se evalúan calidad y ayuda por separado. Las
entregas serán públicas; las evidencias y la explicación deben corresponder a tu caso.
