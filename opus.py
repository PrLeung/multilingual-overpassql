from transformers import pipeline
from tqdm import tqdm

pipe = pipeline("translation", model="KennStack01/Helsinki-NLP-opus-mt-en-zh",device="cuda:0")

if __name__=="__main__":
    input_file="src/src.txt"
    output_file="opus_result/hyp.txt"
    with open(input_file, 'r', encoding='utf-8') as file:
        english_sentences = file.readlines()

    # Translate each English sentence to Chinese and write to the specified translated dataset file
    with open(output_file, 'a+', encoding='utf-8') as file:
        for i, sentence in enumerate(tqdm(english_sentences)):
            if i+1<=4638:
                continue
            # print(i + 1)
            # Translate the sentence
            chinese_translation = pipe(sentence)
            chinese_translation=chinese_translation[0]['translation_text'].replace('\n','')
            # Write the translated sentence to the file
            file.write(chinese_translation + '\n')

            file.flush()