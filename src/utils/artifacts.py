import os
from datetime import datetime


def take_screenshot(driver, name_prefix="twitch"):
    os.makedirs("screenshots", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name_prefix}_{ts}.png"
    driver.save_screenshot(path)
    return path