"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words

file=open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_seperator.txt", 'w', encoding="utf-8")
file.write('\n'.join(generate_words(3)))
        
file.close()
file=open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_seperator.txt", 'r', encoding="utf-8")
print(file.read())    

file=open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_seperator1.txt", 'w', encoding="CP1252")
file.write(','.join(generate_words(3)))
        
file.close()
file=open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_seperator1.txt", 'r', encoding="CP1252")

print(file.read())  