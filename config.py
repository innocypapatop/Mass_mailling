import re
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN", "")
SUDO = list(map(getenv("SUDO", "7507408570,7335094257").split(",")))
