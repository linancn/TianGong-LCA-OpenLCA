# 用于读取文件内容的函数
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


# 用于解析键值对的函数
def parse_key_values(lines):
    return dict(line.strip().split("=") for line in lines if line.strip())
    # key_values = {}
    # for line in lines:
    #     if line.strip():
    #         parts = line.strip().split("=")
    #         if len(parts) == 2:
    #             key_values[parts[0]] = parts[1]
    #         else:
    #             print(f"Skipping invalid line: {line}")
    # return key_values

# 读取messages文件
file1_lines = read_file("properties-raw/messages_zh_tw.properties")#properties-raw/bundle_zh_tw.properties #properties-raw/messages_zh_tw.properties
file2_lines = read_file("properties-raw/messages.properties")#properties-raw/bundle.properties #properties-raw/messages.properties

# 解析键值对
file1_key_values = parse_key_values(file1_lines)
file2_key_values = parse_key_values(file2_lines)

# 找出只在文件1中的键值对
unique_to_file2 = {
    k: v for k, v in file2_key_values.items() if k not in file1_key_values
}

# 写入新messages文件
with open("properties-raw/messages_zh_tw_new.properties", "w", encoding="utf-8") as new_file:
    for key, value in unique_to_file2.items():
        new_file.write(f"{key}={value}\n")

# # 读取bundle文件
# file1_lines = read_file("properties-raw/bundle_zh_tw.properties")#properties-raw/bundle_zh_tw.properties #properties-raw/messages_zh_tw.properties
# file2_lines = read_file("properties-raw/bundle.properties")#properties-raw/bundle.properties #properties-raw/messages.properties

# # 解析键值对
# file1_key_values = parse_key_values(file1_lines)
# file2_key_values = parse_key_values(file2_lines)

# # 找出只在文件2中的键值对
# unique_to_file2 = {
#     k: v for k, v in file2_key_values.items() if k not in file1_key_values
# }

# # 写入新文件
# with open("properties-raw/bundle_zh_tw_new.properties", "w", encoding="utf-8") as new_file:
#     for key, value in unique_to_file2.items():
#         new_file.write(f"{key}={value}\n")
