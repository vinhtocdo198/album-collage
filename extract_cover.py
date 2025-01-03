from PIL import Image, ImageDraw, ImageGrab
import argparse, time

# Parse the album name from the command line
parser = argparse.ArgumentParser()
parser.add_argument("album_name", type=str, help="Name of the album")
args = parser.parse_args()

# Wait for the Spotify window to be in focus
delay_time = 3
time.sleep(delay_time)

# Take a full screenshot
screenshot = ImageGrab.grab()

square_size = 640.5

# Coordinates for the center crop
screen_width, screen_height = screenshot.size  # For 1920x1080 resolution
left = 639.5
top = 159.5
right = left + square_size
bottom = top + square_size

cropped = screenshot.crop((left, top, right, bottom))

# Create a mask for rounded corners
radius = 12  # Adjust for corner roundness
mask = Image.new("L", cropped.size, 0)  # "L" mode for greyscale (used as mask)
draw = ImageDraw.Draw(mask)

# Draw a rounded rectangle on the mask
draw.rounded_rectangle(
    (0, 0, cropped.size[0], cropped.size[1]), radius=radius, fill=255
)
rounded_cropped = Image.new("RGBA", cropped.size)
rounded_cropped.paste(cropped, (0, 0), mask)

# Run using `python extract_cover.py "album_name"`
rounded_cropped.save(f"Covers/{args.album_name}.png")
