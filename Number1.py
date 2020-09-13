def listdict(input_list):
    list_word = ["hot", "dot", "dog", "lot", "log"]
    listsimwrd = []
    listnewword = []
    outputlist = []
    status = True

    newinput_list = input_list.split()

    for i in newinput_list:
        if i not in list_word:
            cntwrngwrd = 0
            spliti = list(i)
            for j in list_word:
                cntwrngcrt = 0
                slicej = list(j)
                for x, y in zip(spliti, slicej):
                    if x != y:
                        cntwrngcrt += 1
                if cntwrngcrt == 1:
                    listsimwrd.append(j)
                    listnewword.append(i if i else '')
                elif cntwrngcrt > 1:
                    cntwrngwrd += 1
            if len(list_word) == cntwrngwrd:
                status = False
                break
        else:
            listnewword.append('')
            listsimwrd.append(i)

    if status:
        for idx, item in enumerate(listnewword):
            if idx == 0:
                if item != '':
                    outputlist.append(item)
                newindex = []
                for index, exsist in enumerate(list_word):
                    if exsist in listsimwrd:
                        newindex.append(index)

                for index, newchar in zip(range(newindex[0], newindex[1] + 1), list_word):
                    outputlist.append(newchar)
            elif idx == 1:
                if item != '':
                    outputlist.append(item)

        print(outputlist)
    else:
        print('You dont have anything')


if __name__ == '__main__':
    print('Enter your list:')
    input_list = input()
    listdict(input_list)
