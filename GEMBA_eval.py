import os
from openai import OpenAI
import re
import argparse
import time

# Define your OpenAI API key
api_key = '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'
re_template=['1|一|one','2|二|two','3|三|three','4|四|four','5|五|five']


# Set up OpenAI API
client = OpenAI(api_key=api_key)

def get_prompt(type,source_lang, target_lang, source_seg, target_seg):
    if type=="CLASS":
        return f"""Classify the quality of translation from {source_lang} to {target_lang} into one of following classes: "No meaning preserved", "Some meaning preserved, but not understandable", "Some meaning preserved and understandable", "Most meaning preserved, minor issues", "Perfect translation".
        {source_lang} source: "{source_seg}"
        {target_lang} translation: "{target_seg}"
        Class:
        """
    elif type=="STAR":
        return f"""Score the following translation from {source_lang} to {target_lang} with one to five stars. Where one star means "Nonsense/No meaning preserved", two stars mean "Some meaning preserved, but not understandable", three stars mean "Some meaning preserved and understandable", four stars mean "Most meaning preserved with possibly few grammar mistakes", and five stars mean "Perfect meaning and grammar".
{source_lang} source: "{source_seg}"
{target_lang} translation: "{target_seg}"
Stars:
        """
    elif type=="SCORE":
        return f"""
    Score the following translation from {source_lang} to {target_lang} on a continuousscale from 0 to 100 that starts with "No meaning preserved", goes through "Some meaning preserved", then "Most meaning preserved andfew grammar mistakes", up to "Perfect meaning and grammar".
{source_lang} source: "{source_seg}"
{target_lang} translation: "{target_seg}"
Score (0-100) Only answer score of number:"""

def process(type, response):
    if type=="STAR":
        for i in range(5):
            pattern = re.compile(re_template[i],re.IGNORECASE)
            if pattern.search(response):
                return i+1
    elif type=="SCORE":
        pattern=re.compile(r'\d+')
        match = pattern.search(response)
        if match:
            return match.group()
        else:
            print(response)
            return None
    return response

# Function to translate English sentence to Chinese using GPT-4 API
def call_GPT(type, prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=0.7,
        top_p=1
    )
    try:
        return process(type, response.choices[0].message.content.strip())
    except:
        return "error"


# Function to calculate GPT score (dummy implementation)
def GEMBA(type, source_lang, target_lang, source_seg, target_seg):
    prompt=get_prompt(type, source_lang, target_lang, source_seg, target_seg)
    return call_GPT(type, prompt)


def main(args):
    # Path to the sample folder

    # Paths to the train files
    train_file = args.src
    translated_file = args.hyp
    output_file=os.path.join(args.output, args.type+".txt")
    
    # Read train and translated files
    with open(train_file, "r", encoding="utf-8") as train_f, \
        open(translated_file, "r", encoding="utf-8") as translated_f, \
            open(output_file,"a+", encoding="utf-8") as output_f:
        
        # Iterate over lines in both files simultaneously
        for i, (train_line, translated_line) in enumerate(zip(train_f, translated_f)):
            if i+1<=args.last_end:
                continue
            print(i+1)
            train_text = train_line.strip()
            translated_text = translated_line.strip()
            
            # Call GPTScore function for each pair of texts
            eval_class = GEMBA(args.type,"English",args.language,train_text, translated_text)
            output_f.write(str(eval_class)+"\n")
            output_f.flush()
            time.sleep(0.5)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate English sentences to Chinese using OpenAI's GPT-4 API.")
    parser.add_argument("-src", type=str, help="Path to the dataset file containing English sentences to translate.", required=True)
    parser.add_argument("-hyp", type=str, help="Path to the dataset file containing English sentences to translate.", required=True)
    parser.add_argument("-output", type=str, help="Path to the dataset file containing English sentences to translate.", required=True)
    parser.add_argument("-language", type=str, help="Language of the sentences in the dataset.", required=True)
    parser.add_argument("-last_end", type=int, help="Last end", required=True)
    parser.add_argument("-type", type=str, help="type", required=True)
    args = parser.parse_args()    

    # Call the main function with the parsed arguments
    main(args)