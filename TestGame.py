# Working on a test game.
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
import turtle as t

def getPos(x,y):
    print(x,y)
    return

def main():
    s = t.getscreen()
    s.onclick(getPos)
    t.mainloop()

main()


# class Form(object):
   # def __init__(self, img):
       # self.img = img
   # def __call__(self, x, y):
       # z = self.img.get_array()[int(y), int(x)]
       # return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x,y,z)
        
# data = np.random.random((10,10))

# figure, ax=plt.subplots()
# img = ax.imshow(data, interpolation='none')
# ax.format_coord=Form(img)
# plt.show()

# image = mpimg.imread("SpacePink.png")
# imgplot = plt.imshow(image)
# plt.show()

