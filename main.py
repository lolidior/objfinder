import numpy as np
import cv2

test = cv2.imread("set/test set.jpg")

cv2.imshow("test", test)
def con(img):
    test_np = np.asarray(img)
    new_np = np.zeros((test_np.shape[0],test_np.shape[1]), dtype=float)
    #shape (920, 1380, 3)
    x = 0
    ko = 0.08
    col = [0,255,0]
    for i in range(test_np.shape[0]):
        for j in range(test_np.shape[1]):
            for k in range(test_np.shape[2]):
                x += round(test_np[i][j][k]/255, 3)*10**(2-k)
            new_np[i][j] = round(x/100, 2)
            x = 0

    for i in range(new_np.shape[0]-1):
        for j in range(new_np.shape[1]-1):
            if abs(new_np[i][j] - new_np[i+1][j]) > ko or abs(new_np[i][j] - new_np[i+1][j+1]) > ko or abs(new_np[i][j] - new_np[i][j+1]) > ko:
                test_np[i][j] = col
            #if test_np[i+1][j][0] != 0 or test_np[i][j+1][0] != 0 or test_np[i+1][j+1][0] != 0:
                #test_np[i][j] = img[i][j]
    return test_np



out_np = con(test)

cv2.imshow("new", out_np)



cv2.waitKey(0)
cv2.destroyAllWindows()
