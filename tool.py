from PIL import Image
import os
image = None
save_to_copy = False
path = ""


def start():
    global image
    global save_to_copy
    global path
    print("Welcome to ImageTool!")
    print("Read the readme for all the commands!")
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

        





if __name__ == "__main__":
    start()
