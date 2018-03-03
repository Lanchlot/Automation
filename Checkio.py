def long_repeat(line):
    repeat = [0]

    def longrepeat(text):
        temp = 0
        for index in range(0, len(text)):
            if text[0] == text[index]:
                temp += 1
            else:
                print(repeat[0], end=' ')
                repeat[0] = max(repeat[0], temp)
                print(text[index:])
                long_repeat(text[index:])
        print('返回值')
        return max(repeat[0], temp)
    return longrepeat(line)


if __name__ == '__main__':
    assert long_repeat('sdsffffse')
    assert long_repeat('ddvvrwwwrggg')
