import os
import shutil
import tensorflow as tf

# Create classes seasons
seasons = {
    'spring': ['march', 'april', 'may'],
    'summer': ['june', 'july', 'august'],
    'autumn': ['september', 'october', 'november'],
    'winter': ['december', 'january', 'february']
}

# Download pre-training model
model = tf.keras.applications.ResNet50(weights='imagenet')

# The path to the folder images
image_folder = 'image'

# Iterate through images in a folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Проверка расширения файла
        image_path = os.path.join(image_folder, filename)
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        input_image = tf.keras.preprocessing.image.img_to_array(image)
        input_image = tf.keras.applications.resnet50.preprocess_input(input_image)
        input_image = tf.expand_dims(input_image, axis=0)

        # Getting model predictions
        predictions = model.predict(input_image)
        decoded_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=1)[0]
        _, class_name, _ = decoded_predictions[0]

        # Moving the image to the appropriate season folder
        for season, months in seasons.items():
            if any(month in class_name.lower() for month in months):
                destination_folder = os.path.join(image_folder, season)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(image_path, destination_folder)
                break
