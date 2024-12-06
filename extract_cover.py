from PIL import Image, ImageDraw, ImageGrab

# Take a full screenshot
screenshot = ImageGrab.grab()

# Define the size of the square crop
square_size = 641.5  # Adjust the size as needed

# Calculate the coordinates for the center crop
screen_width, screen_height = screenshot.size  # For 1920x1080 resolution
left = 639.25
top = 159
right = left + square_size
bottom = top + square_size

# Crop the screenshot to a square (left, upper, right, lower)
cropped = screenshot.crop((left, top, right, bottom))

# Create a mask for rounded corners
radius = 12  # Adjust for corner roundness
mask = Image.new("L", cropped.size, 0)  # "L" mode for greyscale (used as mask)
draw = ImageDraw.Draw(mask)

# Draw a rounded rectangle on the mask
draw.rounded_rectangle(
    (0, 0, cropped.size[0], cropped.size[1]), radius=radius, fill=255
)

# Apply the rounded corner mask to the cropped image
rounded_cropped = Image.new("RGBA", cropped.size)  # Create RGBA image for transparency
rounded_cropped.paste(cropped, (0, 0), mask)  # Use mask for rounded corners

# Change album name here
rounded_cropped.save("Covers/beerbongs & bentleys.png")
