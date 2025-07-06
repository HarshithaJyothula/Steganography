import cv2
import numpy as np

# Load stego image
stego = cv2.imread("stego.png")

# Check if loaded
if stego is None:
    print("❌ ERROR: 'stego.png' not found! Run encode.py first.")
    exit()

# Create blank image for decoded output
decoded = np.zeros_like(stego)

# Extract secret data (4 LSBs) and shift to restore brightness
for row in range(stego.shape[0]):
    for col in range(stego.shape[1]):
        for ch in range(3):
            hidden = stego[row, col, ch] & 0b00001111
            decoded[row, col, ch] = hidden << 4

# Save the decoded image
cv2.imwrite("decoded_secret.png", decoded)
print("✅ Secret image extracted successfully as 'decoded_secret.png'")
