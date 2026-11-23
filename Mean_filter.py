
import cv2
import matplotlib.pyplot as plt

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Apply Mean Filter
    mean_filtered = cv2.blur(image, (3, 3))

    # Save the output image
    cv2.imwrite("mean_filtered.jpg", mean_filtered)

    # Display original and filtered images
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = cv2.cvtColor(mean_filtered, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered)
    plt.title("Mean Filtered Image")
    plt.axis("off")

    plt.show()
  
