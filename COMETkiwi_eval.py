from comet import download_model, load_from_checkpoint
import os
import argparse



def read_file(file_path):
    """
    读取文本文件并返回每行的内容列表
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def create_data(train_lines, translation_lines):
    """
    根据train和translation的内容创建data列表
    """
    data = []
    for train, translation in zip(train_lines, translation_lines):
        data.append({"src": train, "mt": translation})
    return data

def get_data(train_file_path, translation_file_path):
    train_lines = read_file(train_file_path)
    translation_lines = read_file(translation_file_path)

    data = create_data(train_lines, translation_lines)
    return data

def output_score(dataset, data):
    output_file="COMET_result/"+dataset
    with open(output_file, 'a+',encoding="utf-8") as f:
        for score in data:
            f.write(str(score)+'\n')

def get_tigerscore(data, dataset):
    model_path = download_model("Unbabel/wmt22-cometkiwi-da")
    model = load_from_checkpoint(model_path)
    model_output = model.predict(data, batch_size=8)
    output_score(dataset, model_output.scores)
    print(model_output.system_score)

def main(args):
    train_file_path=os.path.join("origin", args.dataset+".txt")
    translation_file_path=os.path.join("en-zh", args.dataset+".txt")
    data=get_data(train_file_path, translation_file_path)
    # print(data)
    get_tigerscore(data, args.dataset)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate English sentences to Chinese using OpenAI's GPT-4 API.")
    parser.add_argument("-dataset", type=str, help="Path to the dataset file containing English sentences to translate.", required=True)
    args = parser.parse_args()    

    # Call the main function with the parsed arguments
    main(args)
    

