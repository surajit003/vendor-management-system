from ecommerce.celery_app import celery_app as app


@app.task
def add(x, y):
    print("entered")
    return x + y
