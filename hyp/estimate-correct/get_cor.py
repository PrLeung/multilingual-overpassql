import json

# 假设JSON文件名为data.json
file_name = 'estimate-correct.json'

# 读取JSON文件并提取'cor'字段
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # 确保data是一个列表
        if isinstance(data, list):
            # 提取'cor'字段
            cor_list = [item['cor'] for item in data if 'cor' in item]

            # 将cor列表写入txt文件
            file_name = 'hyp.txt'
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    for item in cor_list:
                        file.write(f"{item}\n")
                print(f"'{file_name}'文件已成功创建。")
            except IOError:
                print(f"写入文件时出错，请检查文件路径和权限。")

        else:
            print("JSON文件的格式不正确，顶层元素应该是一个列表。")
except FileNotFoundError:
    print(f"未找到文件：{file_name}")
except json.JSONDecodeError:
    print(f"解析JSON文件时出错，请检查文件内容是否格式正确。")
