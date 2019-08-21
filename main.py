import os
import shutil
import datetime

cmd = input('>>>> ')

# timestamp = datetime.datetime.today().strftime("%Y%m%d_%H_%M_%S")

# path_save_folder = r"D:\Python\Temp\runic games\torchlight 2\save"
# path_finish_folder = os.getcwd() + "\\" + timestamp

# shutil.copytree(path_save_folder, path_finish_folder)
#
# print(os.listdir(path_finish_folder))

if cmd == 'save' :
    print('save')
elif cmd == 'back' :
    print('back')
else:
    print('error')

