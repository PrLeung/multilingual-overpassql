import os
# 假设TXT文件名为numbers.txt
dataset=["zero-shot"]
type=["STAR"]

for data in dataset:
    for type_name in type:
        # 读取TXT文件并计算均值
        try:
            dir_name = f"E:\\multilingual-overpassql\\GEMBA_result\\{data}\\all"
            file_name=os.path.join(dir_name, type_name+".txt")
            with open(file_name, 'r', encoding='utf-8') as file:
                numbers = [float(line.strip()) for line in file if line.strip().isdigit()]
                average = sum(numbers) / len(numbers) if numbers else 0
            print(f"{data},{type_name}的均值是：{average}")
        except FileNotFoundError:
            print(f"未找到文件：{file_name}")
        except ValueError:
            print(f"文件中包含非数字内容，请确保所有行都是数字。")
