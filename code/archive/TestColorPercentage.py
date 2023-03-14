
import numpy as np
import cv2


img = cv2.imread('C:/users/tobia/OneDrive/Desktop/Testfoto.jpg')

white = [200, 55, 55]  # RGB
diff = 55
boundaries = [([white[2]-diff, white[1]-diff, white[0]-diff],
               [white[2]+diff, white[1]+diff, white[0]+diff])]
# in order BGR as opencv represents images as numpy arrays in reverse order

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    ratio_brown = cv2.countNonZero(mask)/(img.size/3)
    print('white pixel percentage:', np.round(ratio_brown*100, 2))

    cv2.namedWindow('images', cv2.WINDOW_NORMAL)
    cv2.imshow("images", np.hstack([img, output]))
    cv2.waitKey(0)

