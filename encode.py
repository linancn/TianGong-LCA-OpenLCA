#bundle_zh_cn
with open("properties-txt/output_bundle_zh_cn.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode('unicode_escape').decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("properties-correct/bundle_zh_cn.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)


#messages_zh_cn
with open("properties-txt/output_messages_zh_cn.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode('unicode_escape').decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("properties-correct/messages_zh_cn.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)
    

#bundle_zh_tw
with open("properties-txt/output_bundle_zh_tw.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode('unicode_escape').decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("properties-correct/bundle_zh.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)


#messages_zh_tw
with open("properties-txt/output_messages_zh_tw.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode('unicode_escape').decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("properties-correct/messages_zh.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)