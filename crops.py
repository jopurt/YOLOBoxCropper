import os
from PIL import Image

input_folder = r'D:\path\to\input\folder'

output_folder = r'D:\path\to\output\folder'

# choose class for cropping
your_class = 0

for filename in os.listdir(input_folder):

    if filename.endswith('.txt'):
        txt_path = os.path.join(input_folder, filename)
        image_name = os.path.splitext(filename)[0] + '.jpg'
        image_path = os.path.join(input_folder, image_name)

        if not os.path.exists(image_path):
            print(f"нет фото для  {filename}")
            continue

        img = Image.open(image_path)
        image_width, image_height = img.size

        with open(txt_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split()
            class_id = int(parts[0])

            if class_id == your_class:
                x_center, y_center, width, height = map(float, parts[1:])

                x_center_abs = x_center * image_width
                y_center_abs = y_center * image_height
                width_abs = width * image_width
                height_abs = height * image_height

                x_min = int(x_center_abs - width_abs / 2)
                y_min = int(y_center_abs - height_abs / 2)
                x_max = int(x_center_abs + width_abs / 2)
                y_max = int(y_center_abs + height_abs / 2)

                cropped_img = img.crop((x_min, y_min, x_max, y_max))


                output_filename = f"{os.path.splitext(filename)[0]}_crop_{i}.jpg"
                output_path = os.path.join(output_folder, output_filename)
                cropped_img.save(output_path)

