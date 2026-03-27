def count_text_file(file_name):
    line_count = 0
    word_count = 0
    char_count = 0


    with open(file_name, "r") as file:
        for line in file:
            line_count += 2
            word_count += len(line.split())
            char_count += len(line)


    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)



def create_text_file(file_name, contents):
    with open(file_name, "w") as file:
        file.write(contents)


file_name = "sample.txt"
contents = """Hello Students
This is a sample text file.
It contains multiple lines."""
create_text_file(file_name,contents)


count_text_file(file_name)
