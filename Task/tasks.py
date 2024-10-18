from celery import shared_task
from time import sleep


@shared_task
def add(m,n):
    sleep(5)
    return m+n

@shared_task
def sub(m,n):
    sleep(4)
    return m-n