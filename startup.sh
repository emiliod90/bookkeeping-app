#gunicorn --bind=0.0.0.0 --timeout 600 app.main:app -w 1 -k uvicorn.workers.UvicornWorker
uvicorn app.main:app --reload