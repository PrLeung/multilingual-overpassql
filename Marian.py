from transformers import AutoModelWithLMHead, AutoTokenizer, pipeline
from tqdm import tqdm
import torch


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

pipe = pipeline("translation", model="Normal1919/Marian-NMT-en-zh-lil-fine-tune",device="cuda:0")

def translate(src_text):
    return pipe(src_text)

if __name__=="__main__":
    input_file="src/src.txt"
    output_file="Marian_result/hyp.txt"
    with open(input_file, 'r', encoding='utf-8') as file:
        english_sentences = file.readlines()

    # Translate each English sentence to Chinese and write to the specified translated dataset file
    with open(output_file, 'a+', encoding='utf-8') as file:
        for i, sentence in enumerate(tqdm(english_sentences)):
            # Translate the sentence
            chinese_translation = translate(sentence)
            chinese_translation=chinese_translation[0]['translation_text'].replace('\n','')
            # Write the translated sentence to the file
            file.write(chinese_translation + '\n')

            file.flush()