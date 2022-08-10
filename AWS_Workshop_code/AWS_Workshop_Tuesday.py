# LAB 1 - A SIMPLE FUNCTION

def hello_world():
    print("Level Up in Tech Rocks!!!")
    
hello_world()


# RETURNING INFORMATION FROM A FUNCTION

def hello_world():
    return "Level Up in Tech is an amazing bootcamp!"
    
greeting = hello_world()
print(greeting)


# INTRO TO BOTO3

import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text="I am learning to code in AWS",
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    
    print(response)

translate_text()



# THE MAIN FUNCTION

import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text="Learning to code Python is fun!",
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response)
    
def main():
    translate_text()
    
if __name__=="__main__":
    main()
    
    
# LAB 4 ARGUMENTS

# Positional Arguments
import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am learning to use all of the AWS Services!','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()
    

# Keyword Arguments

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()
    

# Use dictionaries as keyword arguments
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()