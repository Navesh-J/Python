with open("d:\Projects\Python\FileHandling\ test.txt",'w')as f:
    f.write("my first file\n")
    f.write("this file\n\n")
    f.write("contains four lines\n")
    f.write("contains four lines\n")
with open("d:\Projects\Python\FileHandling\ test.txt",'r')as f:
    # f.read(4)
    for line in f:
        print(line,end='')