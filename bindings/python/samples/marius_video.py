import cv2
import marius_no_matrix
import json
import numpy as np

def open_video(filename, name):
    vid = cv2.VideoCapture(filename)

    count = 0

    success = 1

    image_array = []
    while success:
        success, image = vid.read()
        count += 1
        if success:
            # print(image.shape)

            img_val = marius_no_matrix.image_creator(image)
            image_array.append(marius_no_matrix.matrix_creator(img_val))

    image_array_serializable = convert_to_serializable(image_array)

    with open(name + '.json', 'w') as file:
        json.dump(image_array_serializable, file)

# print(image_array)

def convert_to_serializable(obj):
    """
    Recursively convert numpy arrays to lists for JSON serialization.
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    else:
        return obj

def convert_to_ndarray(obj):
    """
    Recursively convert lists to numpy arrays where applicable.
    """
    if isinstance(obj, list):
        # Attempt to convert to numpy array; if it fails, process recursively
        try:
            return np.array(obj)
        except ValueError:
            # If it can't be converted, recurse for nested lists
            return [convert_to_ndarray(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_to_ndarray(value) for key, value in obj.items()}
    else:
        return obj

def open_file(name):
    # Opening a file
    with open(name + '.json', 'r') as file:
        json_data = json.load(file)
    return json_data

def show(json_data):
    restored_data = convert_to_ndarray(json_data)

    while True:
        for i in range(len(restored_data)):
            marius_no_matrix.show_matrix(restored_data[i])

if __name__ == "__main__":
    file = input("Enter file: ") or "/home/marius/Downloads/smiley.mp4"
    name = input("Enter name: ") or "visualization"
    print("generating...")
    open_video(file, name)
    print("created file!")
    print("viewing...")
    show(open_file(name))
