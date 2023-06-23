import os

OPERATOR_SIGNAL = {'+': 201, '-': 202, '*': 203, '/': 204, '%': 205, '<': 206,
                   '<=': 207, '>': 208, '>=': 209, '==': 210, '!=': 211, '=': 212,
                   '&&': 213, '||': 214, '!': 215, '++': 216, '--': 217}
LIMIT_SIGNAL = {'[': 299, ']': 300, '{': 301, '}': 302, '(': 303, ')': 304, ';': 305, ',': 306}
KEYWORD = {'char': 101, 'int': 102, 'float': 103, 'break': 104, 'const': 105, 'return': 106,
           'void': 107, 'continue': 108, 'do': 109, 'while': 110, 'if': 111, 'else': 112,
           'for': 113, 'main': 114}

NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '_']

def main():

    with open('test.txt', 'r') as f:
        text = f.readlines()
        print(text)
        for line in text:
            part_list = line.strip('\n').strip('\t').split(' ')
            print(part_list)

            if part_list != ['']:
                end_sign = False
                for part in part_list:
                    if len(part) >= 1 and ';' in part[-1]:
                        end_sign = True
                        part = part.strip(';')
                    if part in KEYWORD.keys():
                        print(part, KEYWORD[part])
                    elif part in LIMIT_SIGNAL.keys():
                        print(part, LIMIT_SIGNAL[part])
                    elif part in OPERATOR_SIGNAL.keys():
                        print(part, OPERATOR_SIGNAL[part])
                    elif is_char(part):
                        print(part, '222')
                    elif is_int(part):
                        print(part, '223')
                    elif is_float(part):
                        print(part, '224')
                    else:
                        is_combined_string(part)
                    if end_sign:
                        print(';', '305')


def is_char(text):
    flag = False
    if len(text) >= 1 and text[0] in CHAR:
        for each_char in text:
            if each_char in CHAR or each_char in NUM:
                flag = True
            else:
                flag = False
                break
    else:
        flag = False
    return flag


def is_int(text):
    flag = False
    for each_char in text:
        if each_char in NUM:
            flag = True
        else:
            flag = False
            break
    return flag


def is_float(text):
    count_num = 0
    count_sign = 0
    flag = False
    for each_char in text:
        if each_char in NUM:
            count_num += 1
        if each_char == '.':
            count_sign += 1
        else:
            flag = False
    if count_sign == 1 and count_num == len(text) - 1:
        flag = True
    else:
        flag = False
    return flag

def is_combined_string(text):
    state = 0
    res_num = ''
    res_char = ''
    res_operator = ''
    for index in range(len(text)):
        if text[index] in LIMIT_SIGNAL:
            state = 1
            print(text[index], LIMIT_SIGNAL[text[index]])
        elif text[index] in NUM:
            if state == 2:
                res_num += text[index]
            else:
                state = 2
                res_num = ''
                res_num += text[index]
            if (index + 1 < len(text) and text[index + 1] not in NUM) or index == len(text) - 1:
                print(res_num, '223')
                res_num = ''
        elif text[index] in CHAR:
            if state == 3:
                res_char += text[index]
            else:
                state = 3
                res_char = ''
                res_char += text[index]
            if (index + 1 < len(text) and text[index + 1] not in CHAR) or index == len(text) - 1:
                print(res_char, '222')
                res_char = ''
        elif text[index] in OPERATOR_SIGNAL:
            if state == 4:
                res_operator += text[index]
            else:
                state = 4
                res_operator = ''
                res_operator += text[index]
            '''运算符结尾'''
            if (index + 1 < len(text) and text[index + 1] not in OPERATOR_SIGNAL) or index == len(text) - 1:
                print(res_operator, OPERATOR_SIGNAL[res_operator])
                res_char = ''
        else:
            print('error')


main()

