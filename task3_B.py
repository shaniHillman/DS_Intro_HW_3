def longest_words(file):
    try:
        lst_max = ["", "", "", "", ""]
        fhand = open(file)
        for line in fhand:
            new_line = line.rstrip('\n---.,')
            new_line =new_line.replace(".", " ")
            new_line = new_line.replace(",", " ")
            for word in new_line.split():
                #print(word)
                #index of the shortest word in the list of longests words
                index = findShortest(lst_max)
                if len(word) > len(lst_max[index]):
                    lst_max[index]=word
        dict = {}
        for x in range(len(lst_max)):
            dict[lst_max[x]] = len(lst_max[x])
            # print(dict)
        return (sorted(dict, key=dict.get, reverse=True))

    except:
        print("file not found")
        return []

#the function gets list of words
#and returns the index of the shortest word in the list
def findShortest(lst):
    length = len(lst)
    short = len(lst[0])
    ret = 0
    for x in range(0, length):
        if len(lst[x]) < short:
            short = len(lst[x])
            ret = x
    return ret

print(longest_words('ex3_text.txt'))
print(longest_words('ex4_text.txt'))
