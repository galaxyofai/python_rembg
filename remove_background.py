import rembg
from PIL import Image




def remove_background(image_path):
   

    # Load the image
    image = Image.open(image_path)
    

    # Remove the background 
    output = rembg.remove(image)

    # Save the output image

    output.save('output_image_2.png')

    return True

img_path="./giraffe-g8f822d243_1280.jpg"
remove_background(image_path=img_path)




