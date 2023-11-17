#!/bin/bash

# Kiểm tra xem đã truyền đúng số lượng tham số dòng lệnh
if [ "$#" -ne 1 ]; then
    echo "Sử dụng: $0 <tên_file.rpt>"
    exit 1
fi

# Tên file đầu vào được truyền dưới dạng tham số dòng lệnh
input_file="$1"

# Thực hiện lệnh grep và ghi kết quả vào tệp chỉnh sửa
less "$input_file" | sed 's/class_id = 0/\nclass_id = 0/g' | grep -B85 "mAP@" >"I$input_file"
mv "I$input_file" "$input_file"
