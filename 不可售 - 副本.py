import pandas as pd

# SKU
replacements = """

"""

# 门店编号
prefixes = """



"""

# 将数据按行分割并去除空行
replacements_list = [line.strip() for line in replacements.strip().split('\n') if line.strip()]
prefixes_list = [line.strip() for line in prefixes.strip().split('\n') if line.strip()]

# 创建一个空的 DataFrame
data = []

# 添加标题行
columns = ["门店编号(必填)", "sku编码", "商家sku编码(与SKU编码不可同时为空)", "可售状态(可售/不可售)", "现货库存", "门店价格(单位：元)"]

# 填充数据
for prefix in prefixes_list:
    for replacement in replacements_list:
        data.append([prefix, replacement, "", "不可售", 0, 99999])  # 默认价格设置为 99999

# 创建 DataFrame
df = pd.DataFrame(data, columns=columns)

# 将 DataFrame 保存为 Excel 文件
df.to_excel('output.xlsx', index=False)

print("内容已写入 output.xlsx")
