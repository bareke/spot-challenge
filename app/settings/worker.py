from celery import Celery

from .environment import settings

celery = Celery(__name__)
celery.config_from_object(settings.get("celery"))
