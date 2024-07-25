# Provided code removes alphanumeric words from a text file. It reads the content of the file,filters out alphanumeric words, joins the remaining words into a string, and then writes the updated content back to the same file.


def alpha(path):
    with open(path, 'r') as f:
        content = f.read()

    words = content.split()
    non_alphanumeric_word = [i for i in words if not i.isalnum()]

    updated_content = ' '.join(non_alphanumeric_word)

    with open(path, 'w') as f:
        f.write(updated_content)

path='test.txt'
alpha(path)