var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '',
    '/offline',
    '/static/main/css/style.css',
    '/static/main/vendor/bootstrap/css/bootstrap.min.css',
    '/static/main/vendor/icofont/icofont.min.css',
    '/static/main/vendor/boxicons/css/boxicons.min.css',
    '/static/main/vendor/remixicon/remixicon.css',
    '/static/main/vendor/venobox/venobox.css',
    '/static/main/vendor/owl.carousel/assets/owl.carousel.min.css',
    '/static/main/vendor/aos/aos.css',

];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
}); 
