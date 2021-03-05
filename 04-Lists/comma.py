spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(my_list):
    res = ''
    for word in my_list:
        if my_list.index(word) == len(my_list) - 1:
            res += 'and ' + word
        else:
            res += word + ', '
    return res


msg = comma_code(['coffee', 'tea', 'beer', 'soda', 'juice', 'milk', 'smoothie'])
print(msg)