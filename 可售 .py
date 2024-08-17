import pandas as pd


#注释：sku和价格必须对应，中间不要空行，我是拿表格来对的

# SKU
replacements = """
您的sku1
您的sku2

这句话自己删除
"""

# 门店编号
prefixes = """
您的门店1
您的门店2
"""
# 价格
suffixes = """
您的sku1对应的价格1
您的sku2对应的价格2
"""


0# 将数据按行分割并去除空行
replacements_list = [line.strip() for line in replacements.strip().split('\n') if line.strip()]
prefixes_list = [line.strip() for line in prefixes.strip().split('\n') if line.strip()]
suffixes_list = [line.strip() for line in suffixes.strip().split('\n') if line.strip()]

# 创建一个空的 DataFrame
data = []

# 添加标题行
columns = ["门店编号(必填)", "sku编码", "商家sku编码(与SKU编码不可同时为空)", "可售状态(可售/不可售)", "现货库存", "门店价格(单位：元)"]

# 填充数据
for prefix in prefixes_list:
    for replacement, suffix in zip(replacements_list, suffixes_list):
        data.append([prefix, replacement, "", "可售"#这个是可售，可以改不可售, 2, suffix])

        

# 创建 DataFrame
df = pd.DataFrame(data, columns=columns)

# 将 DataFrame 保存为 Excel 文件
df.to_excel('output.xlsx', index=False)

print("内容已写入 output.xlsx")
