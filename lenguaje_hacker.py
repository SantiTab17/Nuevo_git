def hackerLanguage():
    leek_dictionary = {
        'a': '4', 'b': '13', 'c':'[', 'd':')', 'e':'3', 'f':'|=', 'g':'&', 'h':'#', 'i':'1', 'j':',_|', 'k':'>|', 
        'l':'1', 'm':'/\/\\', 'n':'^/', 'o':'0', 'p':'|*', 'q':'(_,)', 'r':'12', 's':'5', 't':'7', 'u':'(_)', 'v':'\/',
        'w':'\/\/', 'x':'><', 'y':'j', 'z':'2',
        '1':'L', '2':'R', '3':'E', '4':'A', '5':'S', '6':'b', '7':'T', '8':'B', '9':'g', '0':'o'
        }

    print("introuzca el texto que quiere traducir:\n")
    text = input()

    output = ""
    
    for i in text:
        for k,v in leek_dictionary.items():
            if k == i.lower():
                output+= v

    print(output)

hackerLanguage()