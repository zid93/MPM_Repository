def palindrom(sample_input):
    max_loop = (int('9' * sample_input)+1)
    highest_palindrom = 0

    for i in range(1, max_loop):
      for j in range(1, max_loop):
        total = i * j
        is_palindrom = (str(total) == str(total)[::-1])
        if is_palindrom and highest_palindrom <= total:
          highest_palindrom = total

    print(highest_palindrom)


if __name__ == '__main__':
    print('Enter your number:')
    input_list = input()
    palindrom(int(input_list))