import os
import shutil
import random

# Set the directory where the dataset is stored
dataset_directory = 'ISL_Sign_Language/'

# Directories for training and testing datasets
train_directory = 'ISL_Sign_Language_Train/'
test_directory = 'ISL_Sign_Language_Test/'

# Define the split ratio for training and testing sets (e.g., 80% for training, 20% for testing)
train_ratio = 0.8

# Create the train and test directories if they do not exist
if not os.path.exists(train_directory):
    os.mkdir(train_directory)

if not os.path.exists(test_directory):
    os.mkdir(test_directory)

# Loop through each class (A-Z and words) in the dataset
for label in os.listdir(dataset_directory):
    # Get the path for the current label (e.g., A, B, C, ..., thank_you, welcome, etc.)
    label_path = os.path.join(dataset_directory, label)

    # Skip if it's not a directory (just for safety)
    if not os.path.isdir(label_path):
        continue

    # Create corresponding directories in the train and test folders
    train_label_path = os.path.join(train_directory, label)
    test_label_path = os.path.join(test_directory, label)

    os.makedirs(train_label_path, exist_ok=True)
    os.makedirs(test_label_path, exist_ok=True)

    # Get the list of all images in the current label directory
    images = os.listdir(label_path)

    # Shuffle the images randomly
    random.shuffle(images)

    # Calculate the split index for training and testing sets
    split_idx = int(len(images) * train_ratio)

    # Split the images into training and testing sets
    train_images = images[:split_idx]
    test_images = images[split_idx:]

    # Move the training images
    for img in train_images:
        img_source = os.path.join(label_path, img)
        img_destination = os.path.join(train_label_path, img)
        shutil.copyfile(img_source, img_destination)

    # Move the testing images
    for img in test_images:
        img_source = os.path.join(label_path, img)
        img_destination = os.path.join(test_label_path, img)
        shutil.copyfile(img_source, img_destination)

    print(f"Processed {label}: {len(train_images)} images for training, {len(test_images)} images for testing")

print("Dataset splitting complete!")
