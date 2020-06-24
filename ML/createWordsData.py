import re
f_dict = open('DICT.txt', 'r', encoding='utf-8')
f_words = open('words.txt', 'w', encoding='utf-8')
f_words.write(str([re.sub('(?:\\n)+', ' ', re.sub('\d+', '', i)) for i in re.findall('(?<!.)(?:[a-zA-Z]+\s{1,10})?[a-zA-Z]+(?:\’[a-zA-Z]+)?(?=(?:\s)+\[)', f_dict.read())]))
f_dict.close()
f_words.close()