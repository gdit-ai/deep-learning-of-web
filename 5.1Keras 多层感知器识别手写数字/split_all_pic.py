from PIL import Image        # array is a numpy array
import numpy as np

im_path = "digits.png"
im1_pil = Image.open(im_path)
#把PIL数据转为numpy类型
im1_nup = np.array(im1_pil)
print(im1_nup.shape)

#print(im1_nup[20][20][0])
#one_pic = im1_nup[0:20,0:20,:]
#count = 0
for num in range(50):
    for col in range(100):
        one_pic = im1_nup[num * 20:num * 20 + 20, col * 20:col * 20 + 20,:]
        c_pil = Image.fromarray(one_pic)
        name = "./pic/" +  str(num * 100 + col) + ".png"
        #count = count + 1
        c_pil.save(name)

s = 0
with open("dig_label.txt","w") as f:
    for num in range(5000):
        f.write(str(num)+ ".png")
        s = int(num/500)
        print(s)
        f.write(" " + str(s))
        f.write("\n")





