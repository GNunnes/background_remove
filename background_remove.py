from rembg import remove
from PIL import Image
from pathlib import Path

# Define input and output paths
input_path = Path(
    "C:/Users/Gustavo/Desktop/LEARNING/GitHub/Background_remove/antes.jpg")
output_path = Path(
    "C:/Users/Gustavo/Desktop/LEARNING/GitHub/Background_remove/depois.png")

# Check if the input file exists
if not input_path.exists():
    print(f"Error: The file {input_path} does not exist.")
else:
    try:
        # Open the input image
        inp = Image.open(input_path)

        # Remove the background
        output = remove(inp)

        # Save the output image
        output.save(output_path)
        print(f"Output saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
