from PIL import Image, ImageDraw

def image_to_pixels(filename):
    """
    (str) -> tuple
    
    Load an image using PIL.Image and extract and return
    the pixels, width, and height as a list.
    """
    img = Image.open(filename)
    
    pixels = img.getdata()
    if (isinstance(pixels[0], tuple)):
        # RGB, convert to lists
        pixels = tuple([rgb_pixel[0:3] for rgb_pixel in pixels])
    else:
        # grayscale, spoof RGB
        pixels = tuple([(pixel,pixel,pixel) for pixel in pixels])
    
    width, height = img.size
    
    return pixels, width, height

def display_image(pixels, width, height, markers=None, filename=None):
    """
    (tuple, int, int, list, str) -> None
    
    Display a tuple of pixels as an image. If markers are provided, draw
    red circles around each 2D coordinate given. If filename given,
    save generated image to file.
    """
    if isinstance(pixels[0],tuple):
        img = Image.new('RGB',(width,height))
        p = pixels
    else:
        img = Image.new('L', (width,height))
        pixels = [min(int(abs(p)),255) for p in pixels]
        p = tuple(pixels)
    
    
    img.putdata(p)
    
    if markers != None:
        draw = ImageDraw.Draw(img)
        rad = max(max(width,height) // 50, 1)
        for marker in markers:
            tl = (marker[0]-rad, marker[1]-rad)
            lr = (marker[0]+rad, marker[1]+rad)
            draw.ellipse(tl + lr, outline='red' )
    
    
    img.show()
    
    if filename != None:
        img.save(filename)


