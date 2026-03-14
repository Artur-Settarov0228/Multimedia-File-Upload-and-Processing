import os
from celery import Celery

# Django settings modulini sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

app = Celery('multimedia_api')

# Django settings dan Celery konfiguratsiyasini olish
app.config_from_object('django.conf:settings', namespace='CELERY')

# Barcha Django app'laridagi tasklarni avtomatik yuklash
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')