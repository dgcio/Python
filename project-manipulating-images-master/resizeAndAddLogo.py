import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'
LIST_IMG_FOLDER = os.listdir('originals')

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in LIST_IMG_FOLDER:
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
            or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself

    print("opening " + filename)
    origIm = Image.open(os.path.join('originals', filename))
    width, height = origIm.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        origIm = origIm.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    origIm.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    # Save changes.
    origIm.save(os.path.join('withLogo', filename))
