with open("output_messages.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode('unicode_escape').decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("messages_zh.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)

