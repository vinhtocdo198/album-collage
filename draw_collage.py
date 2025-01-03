from PIL import Image, ImageDraw
import os

# Get all cover images
image_dir = "Covers"
image_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]
images = [Image.open(os.path.join(image_dir, f)) for f in image_files]

# Define grid size
grid_row = 9
grid_col = 16
grid_size = (grid_row, grid_col)

# Define margin size
margin = 20

# Calculate canvas size with margins
image_width, image_height = images[0].size
canvas_width = grid_size[0] * (image_width + margin) + margin
canvas_height = grid_size[1] * (image_height + margin) + margin

# Create a new blank canvas with white background
canvas = Image.new("RGBA", (canvas_width, canvas_height), (166, 162, 159, 255))

# Paste images onto the canvas with margins
for index, image in enumerate(images):
    x = margin + (index % grid_size[0]) * (image_width + margin)
    y = margin + (index // grid_size[0]) * (image_height + margin)

    # Create a mask for rounded corners
    radius = 12  # Adjust for corner roundness
    mask = Image.new("L", image.size, 0)  # "L" mode for greyscale (used as mask)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, image.size[0], image.size[1]), radius=radius, fill=255
    )

    # Paste the image with the mask to retain rounded corners
    canvas.paste(image, (x, y), mask)

# Convert the canvas to RGB mode for JPEG format
canvas = canvas.convert("RGB")

# Save the final collage
canvas.save("album_collage.jpg", "JPEG")
