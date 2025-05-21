# import csv

# def write_list_to_csv(file_path, data_list):
#     # 打开CSV文件（如果文件不存在则创建）
#     with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
#         # 创建CSV写入器
#         writer = csv.writer(csvfile)
#         # 将列表写入CSV文件的一行
#         writer.writerow(data_list)

# # 示例用法
# data = [1, 2, 3, 4, 5]
# data = ['ab', 'hello']

# write_list_to_csv('z.csv', data)

# #############################

import kagglehub

# Download latest version
# path = kagglehub.dataset_download("/home/fu/Desktop/ubuntu_data/nlp/demo_53_facial_expression_recognition/ResEmoteNet/shuvoalok/raf-db-dataset")
path = kagglehub.dataset_download("shuvoalok/raf-db-dataset")

print("Path to dataset files:", path)