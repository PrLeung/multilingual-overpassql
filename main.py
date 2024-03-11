import argparse
from openai import OpenAI
import time

# Define your OpenAI API key
api_key = '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'

# Set up OpenAI API
client = OpenAI(api_key=api_key)

def get_prompt(shot, language):
    if shot==0:
        return f"You will be provided with a sentence in English, and your task is to translate it into {language}. Try to translate polysemous words into meanings related to architecture or location as much as possible."
    elif shot==2:
        return f"""You will be provided with a sentence in English, and your task is to translate it into {language}. Try to translate polysemous words into meanings related to architecture or location as much as possible. 
    Example:
    Source: florist Forlì-Cesena
    Target: Forlì-Cesena花店
    Source: Ways and nodes with the uid 10074543 newer than yesterday
    Target: 比昨天更新的、uid是10074543的道路和节点
    Source: """

# Function to translate English sentence to Chinese using GPT-4 API
def translate_sentence(sentence, language, shot):
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": get_prompt(shot, language)
            },
            {
                "role": "user",
                "content": sentence
            }
        ],
        temperature=0.7,
        top_p=1
    )
    try:
        return response.choices[0].message.content
    except:
        return "error"

def main(args):
    # Read English sentences from the specified dataset file
    input_file=f"dataset.{args.dataset}.nl"
    output_file=f"translated_dataset.{args.dataset}.{args.language}.{args.shot}.zh"
    with open(input_file, 'r', encoding='utf-8') as file:
        english_sentences = file.readlines()

    # Translate each English sentence to Chinese and write to the specified translated dataset file
    with open(output_file, 'a+', encoding='utf-8') as file:
        for i, sentence in enumerate(english_sentences):
            if i+1<=args.last_end:
                continue
            print(i + 1)
            # Translate the sentence
            chinese_translation = translate_sentence(sentence.strip(), language=args.language, shot=args.shot)
            if chinese_translation == "error":
                break
            chinese_translation=chinese_translation.replace('\n','')
            # Write the translated sentence to the file
            file.write(chinese_translation + '\n')

            file.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate English sentences to Chinese using OpenAI's GPT-4 API.")
    parser.add_argument("-dataset", type=str, help="Path to the dataset file containing English sentences to translate.", required=True)
    parser.add_argument("-language", type=str, help="Language of the sentences in the dataset.", required=True)
    parser.add_argument("-shot", type=int, help="An integer value representing a shot.", required=True)
    parser.add_argument("-last_end", type=int, help="Last end", required=True)
    args = parser.parse_args()    

    # Call the main function with the parsed arguments
    main(args)
