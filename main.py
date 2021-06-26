import os
#file_dir = "C:/Users/user/Downloads/defect_aug_resize_yolo/train/labels"
file_dir = "C:/Users/user/Downloads/defect_aug_resize_yolo/valtest/labels"

file=open("C:/Users/user/Downloads/defect_aug_resize_yolo/valtest/train.txt",'w')
for root, dirs, files in os.walk(file_dir):
    print(root) #當前目錄路徑
    #print(str(dirs) + "\n") #當前路徑下所有子目錄
    #print(str(files) + "\n" )

for i in range(0,len(files)):
    file.write("data/img/" + files[i] + '\n')
    print(files[i] + "\n")