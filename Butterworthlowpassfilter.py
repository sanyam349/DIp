import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", 0)

rows, cols = image.shape
y, x = np.ogrid[:rows, :cols]

D = np.sqrt((y - rows//2)**2 + (x - cols//2)**2)

D0 = 30
n = 2

H = 1 / (1 + (D/D0)**(2*n))

F = np.fft.fftshift(np.fft.fft2(image))
G = F * H

result = np.fft.ifft2(np.fft.ifftshift(G))
output = np.uint8(np.clip(np.abs(result), 0, 255))

cv2.imwrite("butterworth_low_pass.jpg", output)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output, cmap="gray")
plt.title("Butterworth Low Pass")
plt.axis("off")

plt.show()
