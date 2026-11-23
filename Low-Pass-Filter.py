
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found!")

rows, cols = image.shape

dft = np.fft.fftshift(np.fft.fft2(image))

crow, ccol = rows // 2, cols // 2

mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), 30, 1, -1)

filtered = np.fft.ifft2(
    np.fft.ifftshift(dft * mask)
)

output = np.uint8(np.clip(np.abs(filtered), 0, 255))

cv2.imwrite("low_pass_filtered.jpg", output)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output, cmap="gray")
plt.title("Low-Pass Filter")
plt.axis("off")
plt.show()
