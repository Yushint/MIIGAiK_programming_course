import re
import datetime


#text = """23.05.16 я окончил школу. 24/06/2016 я сдал свой последний экзамен.
          #11.08.16 я отправил приказ о зачислении в ВУЗ. И уже 09-01-2016 
          #стал студентом.
        #"""

#text = """23.05.16 21.02.2019 25.06.17 21.12.2020 30.07.2011 30/11/2010"""

text = """Тест от 28.09.21 --> исправлены некоторые ошибки от 2021/09/27."""

text = text.split()

index_list = []
count_patterns = {'pattern_f1': 0, 'pattern_f2' : 0,
                  'pattern_f3' : 0, 'pattern_f4' : 0,
                  'pattern_f5' : 0}

pattern_f1 = re.compile('\d{2}\.\d{2}\.\d{2}')
pattern_f2 = re.compile('\d{2}\.\d{2}\.\d{4}')
pattern_f3 = re.compile('\d{2}/\d{2}/\d{4}')
pattern_f4 = re.compile('\d{2}-\d{2}-\d{4}') 
pattern_f5 = re.compile('\d\d\d\d/\d\d/\d\d')

for i in range(len(text)):
    if re.match(pattern_f2, text[i]):
        count_patterns['pattern_f2'] += 1
        index_list.append(i)
        
    elif re.match(pattern_f1, text[i]):
        count_patterns['pattern_f1'] += 1
        index_list.append(i)
        
    elif re.match(pattern_f3, text[i]):
        count_patterns['pattern_f3'] += 1
        index_list.append(i)
        
    elif re.match(pattern_f4, text[i]):
        count_patterns['pattern_f4'] += 1
        index_list.append(i)
    
    elif re.match(pattern_f5, text[i]):
        count_patterns['pattern_f5'] += 1
        index_list.append(i)

max_pattern = 0
cnt = 0
for key, item in count_patterns.items():
    if item > cnt:
        max_pattern = key
        cnt = item

def make_correct(date):
    if date[2] == '.' and date[5] == '.' and len(date) == 8:
        date = str(datetime.datetime.strptime(date, "%d.%m.%y"))[0:10]
    elif date[2] == '.' and date[5] == '.' and len(date) == 10:
        date = str(datetime.datetime.strptime(date, "%d.%m.%Y"))[0:10]
    elif date[2] == '/' and date[5] == '/' and len(date) == 10:
        date = str(datetime.datetime.strptime(date, "%d/%m/%Y"))[0:10]
    elif date[2] == '-' and date[5] == '-' and len(date) == 10:
        date = str(datetime.datetime.strptime(date, "%m-%d-%Y"))[0:10]
    elif date[4] == '/' and date[7] == '/' and len(date) == 10:
        date = str(datetime.datetime.strptime(date, "%Y/%m/%d"))[0:10]
        
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    
    if max_pattern == 'pattern_f1':
        date = day + '.' + month + '.' + year[-2] + year[-1]
    elif max_pattern == 'pattern_f2':
        date = day + '.' + month + '.' + year
    elif max_pattern == 'pattern_f3':
        date = day + '/' + month + '/' + year
    elif max_pattern == 'pattern_f4':
        date = month + '-' + day + '-' + year
    elif max_pattern == 'pattern_f5':
        date = year + '/' + month + '/' + day
    return date
    
for elem in index_list:
    text[elem] = make_correct(text[elem])
    
print(' '.join(text))

    
    
    


