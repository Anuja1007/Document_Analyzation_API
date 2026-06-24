import cv2


def detect_signature(image_path):
    """
    Basic signature detection using contour analysis.
    Returns True if signature-like patterns are found.
    """

    image = cv2.imread(image_path)

    if image is None:
        return False

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    large_contours = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 200:
            large_contours += 1

    return large_contours > 20