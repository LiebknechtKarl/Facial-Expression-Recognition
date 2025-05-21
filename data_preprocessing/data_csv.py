import os
import pandas as pd

# path = '/path/to/train'
path = '/home/fu/Desktop/ubuntu_data/nlp/demo_53_facial_expression_recognition/ResEmoteNet/raf_dir_li/'
# path = '/home/fu/Desktop/ubuntu_data/nlp/demo_53_facial_expression_recognition/ResEmoteNet/raf_dir_li'
# path = '/home/fu/Desktop/ubuntu_data/nlp/demo_53_facial_expression_recognition/ResEmoteNet/RAF'




label_mapping = {
    "happy": 0,
    "surprise": 1,
    "sad": 2,
    "anger": 3,
    "disgust": 4,
    "fear": 5,
    "neutral": 6
}


for relative_pth in ['train', 'test', 'validation'] :
    image_data = []

    # Make sure the name of the file is partition_iteration_emotion.jpg or .png
    for filename in os.listdir(path + relative_pth):
        if filename.endswith(".jpg") or filename.endswith(".png"):  
            label_name = filename.split('_')[-1].split('.')[0]
            label_value = label_mapping.get(label_name)
            if label_value is not None:  
                image_data.append([filename, label_value])

    df = pd.DataFrame(image_data, columns=["ImageName", "Label"])

    # csv_file_path = 'train_labels.csv'
    csv_file_path = '/home/fu/Desktop/ubuntu_data/nlp/demo_53_facial_expression_recognition/ResEmoteNet/rafdb_csv/' + relative_pth + '_labels.csv'


    df.to_csv(csv_file_path, index=False, header=False)

    print(f"CSV file created at: {csv_file_path}")
