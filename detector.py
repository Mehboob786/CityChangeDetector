import cv2
import numpy as np

def classify_change(region):
    avg_color = np.mean(region, axis=(0, 1))  # BGR average
    b, g, r = avg_color

    if g > r and g > b:
        return "Vegetation Loss"
    elif b > r and b > g:
        return "Water Change"
    else:
        return "New Construction"

def detect_changes(img1, img2, threshold=30):
    img1 = cv2.resize(img1, (512, 512))
    img2 = cv2.resize(img2, (512, 512))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    change_pixels = cv2.countNonZero(thresh)
    total_pixels = thresh.size
    change_percent = (change_pixels / total_pixels) * 100

    output_img = img2.copy()
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = []

    for idx, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)

        # Skip small regions
        if w < 5 or h < 5:
            continue

        region = img2[y:y+h, x:x+w]
        if region.size == 0:
            continue

        change_type = classify_change(region)
        results.append((idx + 1, change_type, x, y, w, h))

        cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        label = f"{change_type}"
        cv2.putText(output_img, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return output_img, diff, thresh, change_percent, results
