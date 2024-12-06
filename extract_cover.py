from PIL import Image, ImageDraw, ImageGrab

# Take a full screenshot
screenshot = ImageGrab.grab()

square_size = 641.5

# Coordinates for the center crop
screen_width, screen_height = screenshot.size  # For 1920x1080 resolution
left = 639.25
top = 159
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

# Change album name here
rounded_cropped.save("Covers/beerbongs & bentleys.png")
