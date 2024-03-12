from transformers import T5ForConditionalGeneration, T5Tokenizer
from tqdm import tqdm
import torch

model_name = 'utrobinmv/t5_translate_en_ru_zh_large_1024'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tokenizer = T5Tokenizer.from_pretrained(model_name)

prefix = 'translate to zh: '

def translate(src_text):
    # translate Russian to Chinese
    input_ids = tokenizer(prefix+src_text, return_tensors="pt")
    input_ids.to(device)
    generated_tokens = model.generate(**input_ids)

    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]

if __name__=="__main__":
    input_file="src/src.txt"
    output_file="T5_result/hyp.txt"
    with open(input_file, 'r', encoding='utf-8') as file:
        english_sentences = file.readlines()

    # Translate each English sentence to Chinese and write to the specified translated dataset file
    with open(output_file, 'a+', encoding='utf-8') as file:
        for i, sentence in enumerate(tqdm(english_sentences)):
            # Translate the sentence
            chinese_translation = translate(sentence)
            chinese_translation=chinese_translation.replace('\n','')
            # Write the translated sentence to the file
            file.write(chinese_translation + '\n')

            file.flush()