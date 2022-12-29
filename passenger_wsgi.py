import sys, os

#INTERP = ".venv/bin/python3"
#if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

environ=os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yooablog.settings')


from yooablog.wsgi import application

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()