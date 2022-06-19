from PIL import Image   

import os


downloads_folder = "C:/Users/Sofi/Desktop/memes/" #aca poner la direccion de la carpeta a donde se encuentran las imagenes

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloads_folder + filename)
            picture.save(downloads_folder + "compressed_"+filename, optimize =True, quality=60) #modificar la calidad a gusto