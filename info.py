import os
import time

class Config(object):
    # Pyrogram Client
    TOKEN = os.environ.get("TOKEN", "8190350217:AAFPBQoEK96Dkg7ILHM9louqXLt6c8SOJUs") # ⚠️ Required
    # Other Configs
    SUDO = list(map(int, os.environ.get("SUDO", "7899610698 7538572906").split()))  # ⚠️ Required
