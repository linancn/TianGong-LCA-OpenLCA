# unicode_string = """
# ActorEditor=\u53c3\u8207\u8005\u7de8\u8f2f
# Actors=\u53c3\u8207\u8005
# Comments=Comments
# Configuration=\u8a2d\u5b9a
# DataProvider=\u8cc7\u6599\u63d0\u4f9b\u8005
# EcoSpold=EcoSpold 1
# ElementaryFlows=\u5143\u7d20\u6d41\u7a0b
# EmptyCategories=\u7a7a\u985e\u5225
# FlowEditor=\u6d41\u7a0b\u7de8\u8f2f
# FlowProperties=\u6d41\u7a0b\u7279\u6027
# FlowPropertyEditor=\u6d41\u7a0b\u7279\u6027\u7de8\u8f2f
# Flows=\u6d41\u7a0b
# GlobalParameters=\u5168\u57df\u53c3\u6578
# ILCDNetworkExport=\u5f9e ILCD \u7db2\u8def\u532f\u51fa
# ILCDNetworkImport=\u5f9e ILCD \u7db2\u8def\u532f\u5165
# ImpactMethodEditor=\u5f71\u97ff\u8a55\u4f30\u65b9\u6cd5\u7de8\u8f2f
# ImpactMethods=\u5f71\u97ff\u8a55\u4f30\u65b9\u6cd5
# ImportEntireDatabase=Import entire database
# ImportEntireDatabase_Info=Import an entire database into the active database.
# ImportExport=\u532f\u51fa/\u532f\u5165
# LCIAMethods=LCIA\u65b9\u6cd5
# Locations=\u4f4d\u7f6e
# Logging=\u7d00\u9304
# Navigation=\u5c0e\u89bd
# NumberFormat=\u6578\u5b57\u683c\u5f0f
# Perspective=\u900f\u8996
# ProcessEditor=\u5de5\u5e8f\u7de8\u8f2f
# Processes=\u5de5\u5e8f
# ProductFlows=\u751f\u7522\u6d41\u7a0b
# ProductSystemEditor=\u751f\u7522\u7cfb\u7d71\u7de8\u8f2f
# ProductSystems=\u751f\u7522\u7cfb\u7d71
# ProjectEditor=\u5c08\u6848\u7de8\u8f2f
# ReportViewer=\u5831\u544a\u95b1\u89bd\u8005
# SearchResults=Search results
# SourceEditor=\u4f86\u6e90\u7de8\u8f2f
# Sources=\u4f86\u6e90
# UnitGroupEditor=\u55ae\u4f4d\u7fa4\u7d44\u7de8\u8f2f
# UnitGroups=\u55ae\u4f4d\u7fa4\u7d44
# Updates=\u66f4\u65b0
# Usage=\u7528\u6cd5
# WasteFlows=\u5ee2\u7269\u6d41\u7a0b
# Welcome=\u6b61\u8fce"""


# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write(unicode_string)


with open("messages_zh_cn.properties", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\n", "@@NEWLINE@@")

encoded_content = content.encode("unicode_escape").decode()

encoded_content = encoded_content.replace("@@NEWLINE@@", "\n")

with open("messages_zh.properties", "w", encoding="utf-8") as f:
    f.write(encoded_content)