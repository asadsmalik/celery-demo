import asyncio
from celery import Task
from asgiref.sync import async_to_sync


class SimpleTask(Task):
    def run(self, *args, **kwargs):
        async_to_sync(asyncio.sleep)(1)
        print("Task running...")
        async_to_sync(asyncio.sleep)(5)
        print("Task finished")
