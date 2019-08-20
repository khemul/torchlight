import os
import shutil

path_save_folder = r"D:\Python\Temp\runic games\torchlight 2\save"
path_finish_folder = os.getcwd() + r"\temp"

shutil.copytree(path_save_folder, path_finish_folder)

print(os.listdir(path_save_folder))

