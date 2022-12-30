from os.path import abspath, dirname, join
import logging
from logging.config import dictConfig
base_dir = abspath(dirname(__file__))
logs_target = join(base_dir + "\logs", "python_logs.log")
