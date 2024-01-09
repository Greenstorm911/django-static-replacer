import re

# i would really apprecite a star or a fork =) <3
def replace_pattern_in_text(input_file, output_file):
    pattern = r'(href|src)="assets/([^"]+)"'
    replacement = r'/\1="{% static "/\2" %}"'
    # removes assets from path and put the rest in the django tag
    
    try:
        with open(input_file, 'r') as infile:
            text_content = infile.read()
        modified_text = re.sub(pattern, replacement, text_content)
        with open(output_file, 'w') as outfile:
            outfile.write(modified_text)
        print("my app is cooking like gordon ramsay", output_file)


    except :
        print("not working properly as it apears make a .txt file in the same directory with the name (input_text.txt)")

if __name__ == "__main__":
    input_file_path = "input_text.txt"
    output_file_path = "output_text.txt"
    replace_pattern_in_text(input_file_path, output_file_path)
