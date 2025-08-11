import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def load_yolo_polygon_annotations(txt_file, img_width, img_height):
    polygons = []
    with open(txt_file, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            if len(parts) < 6 or len(parts) % 2 == 1:
                print(f"Skipping malformed polygon in {txt_file}: {line.strip()}")
                continue
            
            cls_id = int(parts[0])
            coords = list(map(float, parts[1:]))

            poly_points = []
            for i in range(0, len(coords), 2):
                x = int(coords[i] * img_width)
                y = int(coords[i + 1] * img_height)
                poly_points.append((x, y))
            
            polygons.append((cls_id, poly_points))
    return polygons

def visualize_polygon_annotation(image_path, txt_path):    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not load image: {image_path}")
        return
    
    img_height, img_width = img.shape[:2]
    polygons = load_yolo_polygon_annotations(txt_path, img_width, img_height)

    for cls_id, poly_points in polygons:
        poly_array = np.array(poly_points, dtype=np.int32)
        cv2.polylines(img, [poly_array], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.putText(img, f"Class {cls_id}", poly_points[0],
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Convert BGR to RGB for matplotlib visualization
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 8))
    plt.imshow(img_rgb)
    plt.axis("off")
    plt.show()

def main(image_dir, label_dir):    
    if not os.path.exists(image_dir):
        print(f" Image directory does not exist: {image_dir}")
        return
    if not os.path.exists(label_dir):
        print(f" Label directory does not exist: {label_dir}")
        return

    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print(f"No image files found in {image_dir}")
        return

    for img_file in image_files:
        img_path = os.path.join(image_dir, img_file)
        txt_file = os.path.splitext(img_file)[0] + ".txt"
        txt_path = os.path.join(label_dir, txt_file)

        if os.path.exists(txt_path):
            print(f"🔍 Visualizing {img_file} with annotation {txt_file}")
            visualize_polygon_annotation(img_path, txt_path)
        else:
            print(f" No annotation found for {img_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize YOLO polygon annotations on images.")
    parser.add_argument('--image_dir', type=str, required=True,
                        help="Path to the directory containing images.")
    parser.add_argument('--label_dir', type=str, required=True,
                        help="Path to the directory containing YOLO polygon annotation text files.")

    args = parser.parse_args()
    main(args.image_dir, args.label_dir)
