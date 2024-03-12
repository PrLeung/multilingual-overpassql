import os
# 假设TXT文件名为numbers.txt
dataset=["zero-shot","2-shot","estimate-correct"]

for data in dataset:
    # 假设TXT文件名为translations.txt
    dir_name = f"E:\\multilingual-overpassql\\GEMBA_result\\{data}\\subset"
    file_name=os.path.join(dir_name, "CLASS.txt")
    # 初始化一个字典来存储每个类别的计数
    categories_count = {
        "No meaning preserved": 0,
        "Some meaning preserved, but not understandable": 0,
        "Some meaning preserved and understandable": 0,
        "Most meaning preserved, minor issues": 0,
        "Perfect translation": 0
    }

    # 读取TXT文件并统计每个类别的数量
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line in categories_count:
                    categories_count[line] += 1

        # 打印每个类别的计数
        print(data)
        for category, count in categories_count.items():
            print(f"{category}: {count}")

    except FileNotFoundError:
        print(f"未找到文件：{file_name}")
    except IOError:
        print(f"读取文件时出错，请检查文件路径和权限。")
