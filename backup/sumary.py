import os
import pandas as pd

# Đường dẫn đến thư mục chứa các tệp .rpt
folder_path = '/home/trolny/Desktop/PJ2/darknet/backup/'

# Tạo một DataFrame để lưu thông tin
df = pd.DataFrame()

# Tạo 80 mảng để lưu ap của từng class
class_ap = {}
for i in range(1, 80):
    class_ap[f'{i-1}'] = []

# Duyệt qua các tệp .rpt trong thư mục
for file_name in os.listdir(folder_path):
    if file_name.endswith('.rpt'):
        with open(os.path.join(folder_path, file_name), 'r') as file:
            lines = file.readlines()
            

            # Lấy thông tin từ tệp .rpt
            for line in lines:
                if 'class_id' in line:
                    parts = line.strip().split(', ')
                    class_id = int(parts[0].split(' = ')[1])
                    class_name = parts[1].split(' = ')[1]
                    ap = (parts[2].split(' = ')[1].replace('%', ''))
                    class_ap[class_id].append(ap)
    
# Thêm thông tin vào DataFrame
for class_name, ap_values in class_ap.items():
    df[class_name] = ap_values

# Tạo DataFrame cho precision, recall, mAP
precision_recall_map = {
    'precision': [0.56],
    'recall': [0.25],
    'mAP@50': [0.294185]
}

# Thêm thông tin precision, recall, mAP vào DataFrame
df = df.append(precision_recall_map, ignore_index=True)

# Xuất ra tệp Excel
output_excel = '/home/trolny/Desktop/PJ2/darknet/output.xlsx'
df.to_excel(output_excel, index=False)
