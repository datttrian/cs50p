import emoji

def main():
    n = input("Input: ")

    if "," in n:
        n = n.split(",")
        print(n[0] + "," + emo(n[1]))
    else:
        print(emo(n))

def emo(name):
    try:
        o = emoji.emojize(name)
    except:
        pass
    else:
        o = emoji.emojize(name, language='alias')
    return o

main()
