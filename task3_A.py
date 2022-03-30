def read_line(n, file):
    try:
        fhand=open(file)
        count = 0
        if type(n) !=int:
            return ("invalid input detected")
        #count number of lines in file
        file_len = len(fhand.readlines())
        fhand = open(file)
        if n > file_len:
            return "line "+ str(n) + " doesn't exist"
        for line in fhand:
            #print(line)
            count +=1
            if count == n:
                return line.rstrip()
    except:
        return ("file not found")

print(read_line(4, 'ex3_text.txt'))
print(read_line(9, 'ex3_text.txt'))
print(read_line(29, 'ex3_text.txt'))
print(read_line("c", 'ex3_text.txt'))
print(read_line(9, 'ex4_text.txt'))
