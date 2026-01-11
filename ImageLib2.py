
import sys
import subprocess
import os

def check_dependencies():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("PIL not found. Installing Pillow...")
        try:
            # Install the package
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            print("Installation successful. Restarting script to apply changes...")
            print("-" * 50)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception as e:
            print(f"CRITICAL ERROR: Could not install Pillow. Details: {e}")
            sys.exit(1)


check_dependencies()

from PIL import Image, ImageDraw, ImageFont


def toGrid(image):
    pixels = image.load()
    w, h = image.size
    grid = []
    for i in range(w):
        newList = []
        for j in range(h):
            newList.append(pixels[i, j])
        grid.append(newList)
    return grid


def toImage(grid):
    image = Image.new("RGB", (len(grid), len(grid[0])), "white")
    im = image.load()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            im[i, j] = grid[i][j]
    return image
    

def makeGrid(x, y, color = (255, 255, 255)):
    g = []
    for _ in range(x):
        r = []
        for _ in range(y):
            r.append(color)
        g.append(r)
    return g
        


def writeText(image, String, coords, fontSize = 12, fontType = "config/font.ttf", color = (0, 0, 0)):
    # fontType = "arial.ttf"
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontType, fontSize)
    draw.text(coords, String, fill = color, font = font)

