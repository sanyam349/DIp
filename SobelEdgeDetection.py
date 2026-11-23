
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg")

if image is None:
    raise FileNotFoundError("Image not found!")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

magnitude = cv2.magnitude(gx, gy)
edges = cv2.convertScaleAbs(magnitude)

cv2.imwrite("sobel_edges.jpg", edges)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Sobel Edge Detection")
plt.axis("off")
plt.show()
