# LAB 5 - INPUTS

# User input from the console

import boto3
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)
    
kwargs={
    "Text":"I am learning to use Python in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }
    
def main():
    translate_text(**kwargs)
    
if __name__=="__main__":
    main()
    


# The input() function

import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)
    

text = input("Please provide the text you want to have translated: ")
source_language_code = input("Please provide the two letter source language code: ")
target_language_code = input("Please provide the two letter target language code: ")

def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )
        
if __name__=="__main__":
    main()
    
    
    
