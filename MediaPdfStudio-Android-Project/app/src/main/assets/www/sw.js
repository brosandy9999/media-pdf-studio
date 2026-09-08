const CACHE_NAME = 'media-pdf-studio-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './vendor/pdf-lib.min.js',
  './vendor/jszip.min.js',
  './vendor/pdf.mjs',
  './vendor/pdf.worker.mjs'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.map(key => key !== CACHE_NAME ? caches.delete(key) : null)
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(res => res || fetch(e.request))
  );
});
