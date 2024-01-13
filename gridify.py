from PIL import Image

# Load the original image
original_image = Image.open("punks.png")

# Set the size of each small image
tile_size = 24

# Get the dimensions of the original image
original_width, original_height = original_image.size

# Calculate the number of rows and columns
num_rows = original_height // tile_size
num_cols = original_width // tile_size

# Loop through each row and column, and save each small image
for row in range(num_rows):
    for col in range(num_cols):
        # Define the region for the current small image
        left = col * tile_size
        upper = row * tile_size
        right = left + tile_size
        lower = upper + tile_size

        # Crop the region from the original image
        tile = original_image.crop((left, upper, right, lower))

        # Save the small image with a unique name
        tile.save(f"grid_punks/tile_{row}_{col}.png")

print("Images successfully created!")
