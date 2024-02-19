from celery import Celery
from simple_task import SimpleTask

app = Celery('main', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.register_task(SimpleTask())

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'every 5 minutes': {
        'task': 'simple_task.SimpleTask',
        'schedule': 60 * 5,
    },
}