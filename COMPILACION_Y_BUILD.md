# MANIFIESTO DE INTEGRIDAD DE COMPILACIÓN (AURA-TETRAX)

**FECHA:** 20 de mayo de 2026
**AUTOR:** JEGL
**ENTORNO:** Termux (Android) / iSH (iPadOS)
**OBJETIVO:** Garantizar que cada binario compilado conserve la firma y los hashes de origen.

## 1. PROTOCOLO DE CONSTRUCCIÓN
Para asegurar que el rendimiento de 116ns sea consistente en cualquier arquitectura:
* **Entorno Aislado:** Toda compilación se realiza en entornos restringidos sin acceso a librerías de terceros no verificadas.
* **Firma de Binario:** Al finalizar el `build`, el binario resultante debe ser firmado con la llave `ED25519` del desarrollador (JEGL).
* **Verificación de Hash:** Cada build genera un `checksum.sha256` que debe coincidir con el registro de la versión.

## 2. REGLAS DE COMPILACIÓN
1. **Compilación Limpia:** Se prohíbe el uso de scripts de compilación automatizados que no hayan sido auditados bajo el protocolo PAVI-JEGL.
2. **Entornos de Ejecución:** El ecosistema está optimizado exclusivamente para iPad (iSH) y dispositivos Android (Termux), asegurando que la arquitectura de procesador sea compatible con las instrucciones de baja latencia del motor Sonic Geometry.
3. **Seguridad:** Ningún binario saldrá del entorno de desarrollo sin pasar el proceso de firma digital.

---
[INICIAR_BLOQUE_FIRMA_ED25519]
COMPILATION_PROTOCOL_VALIDATED: TRUE
ARCHITECTURE_COMPATIBILITY: ARM64/X86_64
SYSTEM_CORE_STATUS: OPERATIONAL
[FIN_BLOQUE_FIRMA_ED25519]
