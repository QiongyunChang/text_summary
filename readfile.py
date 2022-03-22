import glob
import os

def readfile(path):
    # raed all file in the folder
    # for filename in glob.glob(os.path.join(path, '*.txt')):
       with open(os.path.join(os.getcwd(), filename), 'r') as f:
           try:
               o = f.read()
               r_newlines = o.replace('\n', ' ')
               print(r_newlines,"\n")
            # address different encoding type
           except UnicodeDecodeError :
               with open(os.path.join(os.getcwd(), filename), 'r',encoding='utf-8') as f:
                   o = f.read()
                   r_newlines = o.replace('\n', ' ')
                   print(r_newlines, "\n")

if __name__ == '__main__':
    path = 'D:/qiongyun/desktop/Master/experiment/txt_all'
    for filename in glob.glob(os.path.join(path, '*.txt')):
        readfile(path)