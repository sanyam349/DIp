
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg")

if image is None:
    raise FileNotFoundError("Image not found!")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Laplacian(gray, cv2.CV_64F)
edges = cv2.convertScaleAbs(edges)

cv2.imwrite("laplacian_edges.jpg", edges)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Laplacian Edges")
plt.axis("off")
plt.show()
