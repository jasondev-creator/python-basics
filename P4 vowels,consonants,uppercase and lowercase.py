def count_characters(file_name):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    uppercase_count = 0
    lowercase_count = 0


    with open(file_name, "r") as file:
        text = file.read()


    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1


            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1


    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Uppercase:", uppercase_count)
    print("Lowercase:", lowercase_count)


def create_text_file(file_name,content):
    with open(file_name, "w") as file:
        file.write(content)


file_name = "sample.txt"
content = input("enter few sentences to create a text file with content:")
create_text_file(file_name,content)


count_characters(file_name)
    
