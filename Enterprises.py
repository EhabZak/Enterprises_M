from celery import Celery, chord
from time import sleep

app = Celery ('Enterprises', broker = 'pyamqp://guest:guest@localhost//')

# @app.task
# def reverse(text):
#     sleep(5)
#     return text[::-1]

@app.task
def crawl_enterprises(enterprise_id):
    pass

@app.task
def finalize_output(results):
    pass


enterprise_ids= []

# execute the tasks in parallel
chord(crawl_enterprises.s(enterprise_ids) for enterprise_id in enterprise_ids)(finalize_output.s())
