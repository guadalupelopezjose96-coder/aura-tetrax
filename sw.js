/* * PROTOCOLO LEY ADT - MÓDULO: REALIDAD REAL JEGL
 * PROPIETARIO: JOSÉ EMANUEL GUADALUPE LÓPEZ (JEGL)
 * MARCO LEGAL: STANDARD 1979 / LEY DE EQUIVALENCIA FISCAL
 * ESTADO: 100% PROTEGIDO - PROHIBIDA LA SUPLANTACIÓN VIRTUAL/AUMENTADA
 */

// sw.js - Estatus: 100% v | Justicia Maximisisisima
// Autor: José Emanuel Guadalupe López (JEGL)

const CACHE_NAME = 'fourphonix-core-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/static/manifest.json',
  '/static/icon-192.png',
  '/static/icon-512.png',
  // Agrega aquí tus archivos CSS/JS específicos si los separas del HTML
];

// 1. Fase de Instalación: Creación del Búnker de Almacenamiento
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('✅ Búnker de Caché Abierto al 100%');
        return cache.addAll(ASSETS_TO_CACHE);
      })
      .then(() => self.skipWaiting())
  );
});

// 2. Fase de Activación: Limpieza de Residuos Ilegales
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('🧹 Eliminando Caché Antiguo Ilegal...');
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

// 3. Estrategia de Intercepción: Prioridad de Red con Respaldo de Búnker
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request).catch(() => {
      return caches.match(event.request);
    })
  );
});
