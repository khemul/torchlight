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
path_save_folder = r'D:\Python\Temp\runic games\torchlight 2\save'



def copy_save(path_start):

    timestamp = datetime.datetime.today().strftime("%Y%m%d_%H_%M_%S")
    path_finish_folder = os.path.join(os.getcwd(), 'temp', timestamp)
    print(os.listdir(os.path.join(os.getcwd(), 'temp')))
    shutil.copytree(path_start, path_finish_folder)
    return print('Done!')

def back_save():




if cmd == 'save' :
    copy_save(path_save_folder)
    # print(os.listdir(os.getcwd() + os.path.join('\temp')))
elif cmd == 'back' :
    print('back')
else:
    print('error')


