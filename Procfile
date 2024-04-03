web: gunicorn oc_lettings_site.wsgi
web: gunicorn oc_lettings_site.wsgi --log-file -
web: uwsgi --http :$PORT --module oc_lettings_site.wsgi
web: python manage.py runserver 0.0.0.0:$PORT

