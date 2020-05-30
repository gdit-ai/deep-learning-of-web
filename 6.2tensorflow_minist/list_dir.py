import os
path = r'C:\Users\Administrator\Desktop\SSD-Tensorflow-master\demo'

file_list = os.listdir(path)
print(len(file_list))

for i in file_list:
    if (i[-3:] == 'jpg'):
        print(i)
    # print(i[-3:])

