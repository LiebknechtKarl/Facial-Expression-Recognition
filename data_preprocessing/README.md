# Data Preprocessing  数据预处理

This folder contains the code for data preprocessing. The data preprocessing is done in two steps:
此文件夹包含数据预处理的代码。数据预处理分为两个步骤：


1. `rename.py`: This script renames the files in the dataset to a consistent format. The format is `parition_index_class.jpg`. The script takes the path to the dataset as input and renames the files in the dataset.
`rename.py `：此脚本将数据集中的文件重命名为一致的格式。格式为 `parition_index_class.jpg` 。该脚本将数据集的路径作为输入，并重命名数据集中的文件。


2. `move.py`: This script moves the files in the dataset to a common partitioned directory. That is every image in the `train` partition is in the same `train` folder. The script takes the path to the dataset as input and moves the files to the partitioned directory.
`move.py` 此脚本将数据集中的文件移动到一个公共分区目录中。也就是说， `train` 分区中的每个图像都在同一个`train`文件夹中。该脚本将数据集的路径作为输入，并将文件移动到分区目录中。

## Usage

The current directory structure is as follows:

```
rafdb/
    train/
        angry/
            train_1_aligned.jpg
            train_2_aligned.jpg
            ...
        disgust/
        ...
        |
    test/
        angry/
            test_1_aligned.jpg
            test_2_aligned.jpg
            ...
        disgust/
        ...
        |
    val/
        angry/
            val_1_aligned.jpg
            val_2_aligned.jpg
            ...
        disgust/
        ...
        |
```

Run the `rename.py` script to rename the files in the dataset:

```bash
python rename.py
```

The new directory structure will be as follows:

```
rafdb/
    train/
        angry/
            train_1_angry.jpg
            train_2_angry.jpg
            ...
        disgust/
        ...
        |
    test/
        angry/
            test_1_angry.jpg
            test_2_angry.jpg
            ...
        disgust/
        ...
        |
    val/
        angry/
            val_1_angry.jpg
            val_2_angry.jpg
            ...
        disgust/
        ...
        |
```

Run the `move.py` script to move the files in the dataset to a common partitioned directory:

```bash
python move.py
```

The new directory structure will be as follows:

```
rafdb/
    train/
        train_1_angry.jpg
        train_2_angry.jpg
        train_1_disgust.jpg
        ...
        |
    test/
        test_1_angry.jpg
        test_2_angry.jpg
        test_1_disgust.jpg
        ...
        |
    val/
        val_1_angry.jpg
        val_2_angry.jpg
        val_1_disgust.jpg
        ...
        |
```

## CSV Generation

Run the `data_csv.py` script to generate the CSV file for the dataset:

```bash
python data_csv.py
```

This will generate a CSV file for every partition in the dataset with the following format:

```
image_name class
train_1_angry.jpg 3
train_2_happy.jpg 0
train_3_neutral.jpg 6
...
```

And the directory structure will be as follows:

```
rafdb/
    train/
    train_labels.csv
    test/
    test_labels.csv
    val/
    val_labels.csv
```

The dataset is now ready for training.