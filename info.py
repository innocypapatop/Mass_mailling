import os
import time

class Config(object):
  TOKEN = os.environ.get("TOKEN", "")
  SUDO = list(map(int, os.environ.get("SUDO", "7507408570,7335094257").split(",")))
