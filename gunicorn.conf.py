worker_class = "uvicorn.workers.UvicornWorker"
app_module = "main:app"
proc_name = "spacy_server_app"

workers = 1
threads = 1
daemon = False

errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
loglevel = "info"