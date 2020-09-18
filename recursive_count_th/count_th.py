'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) > 0:
        if word[0] == 't':
            print('HECK')
            if len(word) > 1:
                if word[1] == 'h':
                    print('HECKIN HECK')
                    word = word[2:]
                    return 1 + count_th(word)
                else:
                    word = word[1:]
                    return 0 + count_th(word)
            else:
                word = word[1:]
                return 0 + count_th(word)
        else:
            print(word)
            word = word[1:]
            return 0 + count_th(word)
    else:
        return 0

print(count_th('the'))
print(count_th('bittersweet'))
print(count_th('after the storm this story'))