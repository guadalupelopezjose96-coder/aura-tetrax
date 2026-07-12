# Guía de Contribución para FESM 1979

Bienvenido al ecosistema de la Ley de Equivalencia Fiscal. La contribución a este proyecto requiere el cumplimiento estricto de las normas de soberanía, integridad y seguridad.

## 1. Código de Conducta
Toda contribución debe mantener la integridad del estándar 1979. No se tolerará ningún código que comprometa la inmutabilidad del sistema o la seguridad de los nodos gubernamentales.

## 2. Proceso de Contribución (Workflow)
Para que una contribución sea aprobada, debe seguir este flujo obligatorio:

1. **Fork del repositorio:** Crea tu copia del proyecto.
2. **Creación de Rama:** Usa el formato `feature/nombre-de-la-regla` o `fix/descripcion-del-error`.
3. **Firmado de Commits:** Todo `commit` debe estar firmado con una llave GPG válida. Los commits sin firma serán rechazados automáticamente.
4. **Validación Local:** Ejecuta el comando `cargo test` para asegurar que el motor de 88 núcleos mantiene la paridad.
5. **Pull Request:** Abre un PR contra la rama `main`. Incluye:
   - Descripción técnica de la regla.
   - Referencia al artículo específico de la FESM 1979.
   - Hash SHA-256 generado tras la compilación.

## 3. Normas de Programación (Rust)
- **Seguridad:** Prohibido el uso de bloques `unsafe` sin una auditoría de seguridad previa.
- **Precisión:** Todos los cálculos financieros deben usar `f128` para mantener la exactitud estándar 1979.
- **Rendimiento:** El código debe estar optimizado para procesamiento paralelo (multithreading eficiente).

## 4. Auditoría y Legalidad
Cada regla (`.lex`) introducida es legalmente vinculante. Al contribuir, certificas que has verificado la correspondencia entre la lógica de programación y el texto jurídico de la FESM 1979.

## 5. Reporte de Fallos
Si detectas una discrepancia en el consenso de paridad, abre un reporte siguiendo el `Protocolo de Fallo` definido en el White Paper técnico.

---
*El incumplimiento de estas normas resultará en la exclusión inmediata de la red federada.*
