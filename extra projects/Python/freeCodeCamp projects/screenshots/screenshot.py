import pyscreenshot as ImageGrab
from datetime import datetime

def take_screenshot():
    print("Taking screenshot...")
    image_name = f"screenshot-{str(datetime.now())[:19]}"
    screenshot = ImageGrab.grab()

    filepath = f"./sc/{image_name}.png"
    screenshot.save(filepath)

    print("Screenshot taken...")

    return filepath

take_screenshot()