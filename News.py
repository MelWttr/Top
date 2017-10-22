import chardet
import re
import string
import collections

def decode_file(file_name):                    # Раскодирует файл
  with open(file_name, "rb") as f:
        data = f.read()
        res = chardet.detect(data)
        file = data.decode(res["encoding"])
        file = file.lower().strip()
        return(file)

def string_parsing(data):                       # Убирает пунктуацию из текста
  regexp = '[{}]*'.format(string.punctuation)
  return re.sub(regexp, '', data)

def  top_ten(text):                             # Возвращает список 10 самых популярных слов
  # counter = collections.Counter()
  words = text.split()
  words_new = []
  for word in words:
      if len(word) > 6:
          words_new.append(word)
  words = collections.Counter(words_new).most_common(11)
  return(words)

def print_result(list):                         # Печатает топ 10
  for i in range(len(list)-1):
    print("{0} - {1}".format(i+1, list[i][0]))

countries = ["Африка", "Кипр", "Франция", "Италия"]
for country in countries:
    print("{0}:".format(country))
    if country == "Африка":
        s = "newsafr.txt"
        print_result(top_ten(string_parsing(decode_file(s))))
    elif country == "Кипр":
        s = "newscy.txt"
        print_result(top_ten(string_parsing(decode_file(s))))
    elif country == "Франция":
        s = "newsfr.txt"
        print_result(top_ten(string_parsing(decode_file(s))))
    elif country == "Италия":
        s = "newsit.txt"
        print_result(top_ten(string_parsing(decode_file(s))))


