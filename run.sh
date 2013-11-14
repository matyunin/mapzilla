uwsgi --socket /tmp/mapzilla_uwsgi.sock --wsgi-file mapzilla.py --callable app --processes 4 --threads 2 --uid redneck --master
