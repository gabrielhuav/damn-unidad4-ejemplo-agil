# Flujo del incremento

1. Ordenar el backlog por valor, riesgo y dependencias. Conversar cada historia y completar sus criterios.
2. Seleccionar un objetivo del Sprint y pocas historias que quepan en dos semanas. Estimar con planning poker; los puntos no son horas ni una medida de productividad individual.
3. Configurar Puntos e Iteracion en Projects. Usar Todo, In Progress, En revision y Done. Límite acordado: dos historias en desarrollo; es una política del equipo, no una restricción automática del tablero.
4. Crear una rama ligada al issue, por ejemplo feat/1-ubicacion. Hacer commits pequeños y pruebas.
5. Abrir un PR con el issue, explicación, pruebas y evidencias. Mover a En revision.
6. Otra persona revisa el cambio. El autor responde comentarios. CI y aprobación son evidencias distintas.
7. Integrar cuando se cumpla la [definición de terminado](definicion_de_terminado.md). Un integrante sin otra persona revisora no debe fingir aprobación.
8. Hacer Review del incremento y retrospectiva del proceso. Registrar lo aprendido y crear acciones con responsable.

## Trazabilidad

Issue → rama → commits → PR → pruebas → revisión → integración → versión demostrable.

## Pruebas del caso móvil

- Ubicación: concedido, denegado, aproximado, servicio apagado y dato antiguo.
- Foto: selección, cancelación, error y envío interrumpido.
- API: contrato, 401, 403, validación, timeout y reintento sin duplicados.
- Nube: reglas por usuario, acceso ajeno rechazado y comportamiento sin red.
- Push: permiso, renovación de token, primer plano/fondo y destino validado.

## Conservación

Los campos y vistas del Project viven en GitHub. Versionar en Git los acuerdos, una exportación cuando se requiera y las evidencias asociadas a cada incremento.
