def longest_words(file):
    try:
        dict = {}
        # lst_max = ["", "", "", "", ""]
        fhand = open(file)
        for line in fhand:
            new_line = line.rstrip('\n-.(,')
            new_line =new_line.replace(".", " ")
            new_line = new_line.replace(",", " ")
            for word in new_line.split():
                dict[word] = len(word)
        #print(dict)
        return sorted(dict, key=dict.get, reverse=True)[:5]
    except:
        print("file not found")
        return []


print(longest_words('ex3_text.txt'))
print(longest_words('ex4_text.txt'))
# ['electromagnetic', 'gravitational', 'Consequently', 'calculations', 'ultraviolet'].