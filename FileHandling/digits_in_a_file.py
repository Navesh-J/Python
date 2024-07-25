#Python program for printing digits present in a file.

def digits(path):
    with open(path,'r',encoding='utf-8') as f:
        content=f.read()
    for i in content:
        if i.isdigit():
            print(i)
path="d:\Projects\Python\FileHandling\ test.txt"
digits(path)