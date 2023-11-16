# 用于读取文件内容的函数
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


# 用于解析键值对的函数
def parse_key_values(lines):
    return dict(line.strip().split("=") for line in lines if line.strip())


# 读取文件
file1_lines = read_file("messages_zh_cn.properties")
file2_lines = read_file("messages.properties")

# 解析键值对
file1_key_values = parse_key_values(file1_lines)
file2_key_values = parse_key_values(file2_lines)

# 找出只在文件1中的键值对
unique_to_file1 = {
    k: v for k, v in file1_key_values.items() if k not in file2_key_values
}

# 写入新文件
with open("new.properties", "w", encoding="utf-8") as new_file:
    for key, value in unique_to_file1.items():
        new_file.write(f"{key}={value}\n")
