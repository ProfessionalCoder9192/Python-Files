import cv2

def draw_dimension_arrow(img, pt1, pt2, color=(0, 255, 0), thickness=2, tip_length=0.05):
    cv2.arrowedLine(img, pt1, pt2, color, thickness, tipLength=tip_length)
    cv2.arrowedLine(img, pt2, pt1, color, thickness, tipLength=tip_length)

def main():
    image_path = "Bg.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not open or find the image '{image_path}'.")
        return

    height, width = img.shape[:2]

    v_start = (int(width / 2), 0)
    v_end = (int(width / 2), height)
    draw_dimension_arrow(img, v_start, v_end, color=(0, 255, 0), thickness=3, tip_length=0.03)

    h_start = (0, int(height / 2))
    h_end = (width, int(height / 2))
    draw_dimension_arrow(img, h_start, h_end, color=(0, 255, 0), thickness=3, tip_length=0.03)

    v_text = f"{height} pixels"
    h_text = f"{width} pixels"

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_thickness = 2

    (v_text_w, v_text_h), _ = cv2.getTextSize(v_text, font, font_scale, font_thickness)
    v_text_x = v_start[0] + 20
    v_text_y = (height // 2) + (v_text_h // 2) - 30

    cv2.putText(img, v_text, (v_text_x + 2, v_text_y + 2), font, font_scale, (0, 0, 0), font_thickness + 2, cv2.LINE_AA)
    cv2.putText(img, v_text, (v_text_x, v_text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    (h_text_w, h_text_h), _ = cv2.getTextSize(h_text, font, font_scale, font_thickness)
    h_text_x = (width // 2) - (h_text_w // 2)
    h_text_y = h_start[1] - 20

    cv2.putText(img, h_text, (h_text_x + 2, h_text_y + 2), font, font_scale, (0, 0, 0), font_thickness + 2, cv2.LINE_AA)
    cv2.putText(img, h_text, (h_text_x, h_text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

    output_path = "Bg_annotated.jpg"
    cv2.imwrite(output_path, img)
    print(f"Success! Annotated image saved as '{output_path}'")

    cv2.imshow("Pixel Length Visualization", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
