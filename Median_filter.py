
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg")

if image is None:
    raise FileNotFoundError("Image not found!")

filtered = cv2.medianBlur(image, 3)
cv2.imwrite("median_filtered.jpg", filtered)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB))
plt.title("Median Filter")
plt.axis("off")
plt.show()
