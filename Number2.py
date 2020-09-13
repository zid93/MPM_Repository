def wordSplit(wordList, word):
    listoutputword = []
    listword = [[False for i in range(len(word))] for x in range(len(word))]
    for i in range(1, len(word) + 1):
        for j in range(len(word) - i + 1):
            if word[j:j + i] in wordList:
                listword[j][j + i - 1] = True
                listoutputword.append(word[j:j + i])
            else:
                for k in range(j + 1, j + i):
                    if listword[j][k - 1] and listword[k][j + i - 1]:
                        listword[j][j + i - 1] = True

    if listword[0][len(word) - 1] == True:
        print(listoutputword)
    else:
        print('Nothing..')

if __name__ == '__main__':
    wordlist = ['pro', 'gram', 'merit','program', 'it', 'programmer']
    print('Enter your list:')
    input_list = input()
    x = wordSplit(wordlist,input_list)
