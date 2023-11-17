with open("properties/messages_zh.properties","r",encoding="utf-8") as f:
    content = f.read()

#解码
with open("output_messages.txt","w",encoding="utf-8") as f:
    f.write(content.encode("utf-8").decode("unicode_escape"))
    

with open("properties/bundle_zh.properties","r",encoding="utf-8") as f:
    content = f.read()

#解码
with open("output_bundle.txt","w",encoding="utf-8") as f:
    f.write(content.encode("utf-8").decode("unicode_escape"))

