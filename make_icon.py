from PIL import Image, ImageDraw

def create_play_icon(filename="play.png", size=(64, 64)):
    # Create a transparent image
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a semi-transparent black circle
    draw.ellipse((0, 0, size[0], size[1]), fill=(0, 0, 0, 180))
    
    # Draw a white play triangle
    triangle = [
        (size[0] * 0.35, size[1] * 0.25),
        (size[0] * 0.35, size[1] * 0.75),
        (size[0] * 0.75, size[1] * 0.5)
    ]
    draw.polygon(triangle, fill=(255, 255, 255, 255))
    
    img.save(filename)

if __name__ == "__main__":
    create_play_icon()
