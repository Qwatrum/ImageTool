from PIL import Image, ImageFilter, ImageEnhance
import PIL
import os

import PIL.Image
image = Image.open("raccoon.jpg")
save_to_copy = True
path = "raccoon.jpg"

def get_average_pixel():
    r = 0
    g = 0
    b = 0
    
    pixels = list(image.getdata())
    for e in pixels:
        r += e[0]
        g += e[1]
        b += e[2]
    
    r /= len(pixels)
    g /= len(pixels)
    b /= len(pixels)
    r = round(r)
    g = round(g)
    b = round(b)

    return r,g,b

def start():
    global image
    global save_to_copy
    global path
    print("Welcome to ImageTool!")
    print("Read the readme for all the commands or type /commands!")
    print("Type a command.")
    
    while True:
        cmd = input("> ")

        if cmd.startswith("/set_picture"):
            try:
                p = cmd.split(" ")[1]
            except IndexError:
                print("Please add a file name!")
                break
            
            try:
                image = Image.open(p)
                path = p
                print("Successful!")
                print("Image is set.")
            except FileNotFoundError:
                print("Path unvalid!")

        elif cmd.startswith("/set_save_to_copy"):
            try:
                b = cmd.split(" ")[1]
            except IndexError:
                print("Please add a boolean!")
                break
            
            if b.lower() == "true":
                save_to_copy = True
                print("Successful!")
                print("Boolean is set.")
            elif b.lower() == "false":
                save_to_copy = False
                print("Successful!")
                print("Boolean is set.")
            else:
                print("Unvalid boolean!")

        elif cmd == "/get_size":
            try:
                print("Size:")
                print(image.size)
            except AttributeError:
                print("Image is not set!")

        elif cmd == "/get_storage":
            try:
                print("Storage size:")
                print(str(os.path.getsize(path)) + " bytes")
            except FileNotFoundError:
                print("Image is not set!")

        elif cmd == "/get_average_pixel":
            print("Average pixel color: ")
            print(get_average_pixel())

        elif cmd == "/invert":
            inverted_image = PIL.ImageOps.invert(image)
            if save_to_copy:
                
                inverted_image.save("inverted_image.png")
            else:
                inverted_image.save(path)
            print("Inverted!")
        
        elif cmd.startswith("/rotate"):
            try:
                d = cmd.split(" ")[1]
            except IndexError:
                print("Please add a direction!")
                break
            
            if d == "right":
                rotated_image = image.transpose(Image.Transpose.ROTATE_90)
            elif d == "left":
                rotated_image = image.transpose(Image.Transpose.ROTATE_270)
            else:
                print("Unknown direction.")
                break

            if save_to_copy:
                
                rotated_image.save("rotated_image.png")
                
            else:
                rotated_image.save(path)
            print("Rotated!")

        elif cmd.startswith("/apply_filter"):
            try:
                i = int(cmd.split(" ")[1])
            except ValueError or IndexError:
                print("Please use a valid index!")
                break
            image_edited = None
            if i == 0:
                image_edited = image.filter(ImageFilter.BLUR)
            elif i == 1:
                image_edited = image.filter(ImageFilter.DETAIL)
            elif i == 2:
                image_edited = image.filter(ImageFilter.EMBOSS)
            elif i == 3:
                image_edited = image.filter(ImageFilter.SHARPEN)
            elif i == 4:
                image_edited = image.filter(ImageFilter.SMOOTH)
            elif i == 5:
                image_edited = image.filter(ImageFilter.CONTOUR)

            if save_to_copy:
                
                image_edited.save("image_filtered.png")
            else:
                image_edited.save(path)

        elif cmd == "/filter_list":
            print("List of filters:")
            print("0: Blur")
            print("1: Detail")
            print("2: Emboss")
            print("3: Sharpen")
            print("4: Smooth")
            print("5: Contour")

        elif cmd == "commands":
            print("/commands" + " - Returns a list of all commands")
            print("/set_picture <file name>" + " - Sets the image with which will be worked")
            print("/set_save_to_copy <true | false>" + " - Whether an edited picture should be saved as a copy")
            print("/get_size" + " - Returns size")
            print("/get_storage" + " - Returns storage size")
            print("/get_avergy_pixel" + " - Returns the color of the average pixel")
            print("/rotate <right | left>" + " - Rotates the image right or left")
            print("/invert" + " - Inverts the image")
            print("/apply_filter <0-5>" + " - Applies a filter")
            print("/filter_list" + " - Returns a list of available filters")

        
        else:
            print("Unknown command!")

        



if __name__ == "__main__":
    start()