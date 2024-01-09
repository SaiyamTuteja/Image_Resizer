import cv2

source = r"saiyam.jpg"
destination = "new_saiyam.png"
scale_percent =50

# Load the image and check if it's successfully loaded
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
if src is None:
    print(f"Error: Unable to read the image at {source}")
else:
    new_width = int(src.shape[0] * scale_percent / 100)
    new_height = int(src.shape[1] * scale_percent /100)
    output = cv2.resize(src, (new_width, new_height))
    cv2.imwrite(destination, output)
    cv2.waitKey(0)
