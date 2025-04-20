from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont
import time

# Initialize display
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Load default font
font = ImageFont.load_default()

# Display message for 10 seconds
with canvas(device) as draw:
    draw.text((10, 25), "Hello from Pi!", font=font, fill=255)

time.sleep(10)

# Clear screen
device.clear()
