"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
f=open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_1.txt","r")
print(f.read())

f1 = open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_99.txt", "w")
f1.write('12,22,33,44,55')
f1.close()

f1 = open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\files\file_99.txt", "r")
print(f1.read())