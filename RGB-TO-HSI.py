
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg")

if image is None:
    raise FileNotFoundError("Image not found!")

# Convert BGR to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rgb = rgb.astype(np.float32) / 255.0

R = rgb[:, :, 0]
G = rgb[:, :, 1]
B = rgb[:, :, 2]

# Calculate Hue
num = 0.5 * ((R - G) + (R - B))
den = np.sqrt((R-G)**2 + (R-B)*(G-B))

theta = np.zeros_like(R)
valid = den > 1e-8

ratio = np.zeros_like(R)
ratio[valid] = np.clip(num[valid] / den[valid], -1, 1)

theta[valid] = np.arccos(ratio[valid])

H = theta.copy()
H[B > G] = 2 * np.pi - H[B > G]
H = H / (2 * np.pi)

# Calculate Saturation
total = R + G + B
minimum = np.minimum(np.minimum(R, G), B)

S = np.zeros_like(R)
nonzero = total > 1e-8
S[nonzero] = 1 - (3 * minimum[nonzero] / total[nonzero])

# Calculate Intensity
I = total / 3

# Convert components into images
H_image = np.uint8(H * 255)
S_image = np.uint8(S * 255)
I_image = np.uint8(I * 255)

# Save output images
cv2.imwrite("hue_component.jpg", H_image)
cv2.imwrite("saturation_component.jpg", S_image)
cv2.imwrite("intensity_component.jpg", I_image)

# Display results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(rgb)
plt.title("Original RGB Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(H_image, cmap="gray")
plt.title("Hue Component")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(S_image, cmap="gray")
plt.title("Saturation Component")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(I_image, cmap="gray")
plt.title("Intensity Component")
plt.axis("off")

plt.tight_layout()
plt.savefig("rgb_to_hsi_output.png")
plt.show()
