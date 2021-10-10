import datetime

def make_correct(date:str):
    """ Проверяет дату на форматное соответствие.
        Параметр date задаётся в форме 'day.month.year'.
        Печатает дату в правильном формате.
    """
    day = int(date[0] + date[1])
    month = int(date[3] + date[4])
    year = int(date[6] + date[7] + date[8] + date[9])
    if day > 31:
        is_correct = False
        day = 31
    if month > 12:
        is_correct = False
        month = 12
    try: 
        s = str(day) + ' ' + str(month) + ' ' + str(year)
        s = s.replace(' ','.')
        new_date = str(datetime.datetime.strptime(s, "%d.%m.%Y"))[0:10]
        is_correct = True
        new_date = new_date.split('-')
        new_date.reverse()
        return '.'.join(new_date)
    except Exception:
        is_correct = False
    while is_correct == False:
        day -= 1
        try: 
            s = str(day) + ' ' + str(month) + ' ' + str(year)
            s = s.replace(' ','.')
            new_date = str(datetime.datetime.strptime(s, "%d.%m.%Y"))[0:10]
            is_correct = True
            new_date = new_date.split('-')
            new_date.reverse()
            return '.'.join(new_date)
        except Exception:
            is_correct = False        
        
            
def func1(datestring):
    return make_correct(datestring)
    

def func2(s):
    today = str(datetime.datetime.now())[0:10]
    today = today.split('-')
    today.reverse()
    today = '.'.join(today)
    
    tomorrow = str(datetime.datetime.now() +\
                   datetime.timedelta(days=1))[0:10]
    tomorrow = tomorrow.split('-')
    tomorrow.reverse()
    tomorrow = '.'.join(tomorrow)
    
    yesterday = str(datetime.datetime.now() -\
                    datetime.timedelta(days=1))[0:10]
    yesterday = yesterday.split('-')
    yesterday.reverse()
    yesterday = '.'.join(yesterday)
    
    in_a_day = str(datetime.datetime.now() +\
                   datetime.timedelta(days=2))[0:10]
    in_a_day = in_a_day.split('-')
    in_a_day.reverse()
    in_a_day = '.'.join(in_a_day)
    
    before_yesterday_day = str(datetime.datetime.now() -\
                   datetime.timedelta(days=2))[0:10]
    before_yesterday_day = before_yesterday_day.split('-')
    before_yesterday_day.reverse()
    before_yesterday_day = '.'.join(before_yesterday_day)    
    
    s = s.split()
    for i in range(len(s)):
        if s[i] == "сегодня":
            s[i] = today
        elif s[i] == "завтра":
            s[i] = tomorrow
        elif s[i] == "вчера":
            s[i] = yesterday
        elif s[i] == "послезавтра":
            s[i] = in_a_day
        elif s[i] == "позавчера":
            s[i] = before_yesterday_day
    return ' '.join(s)
    
    
def func3(s):
    s = s.split()
    
    monday = datetime.datetime(2021, 9, 27)
    tuesday = datetime.datetime(2021, 9, 28)
    wednesday = datetime.datetime(2021, 9, 29)
    thursday = datetime.datetime(2021, 9, 30)
    friday = datetime.datetime(2021, 10, 1)
    saturday = datetime.datetime(2021, 10, 2)
    sunday = datetime.datetime(2021, 10, 3)
    
    date = ''
    if len(s) == 1:
        if s[0] == "понедельник":
            date = str(monday)[0:10]
        elif s[0] == "вторник":
            date = str(tuesday)[0:10]
        elif s[0] == "среда":
            date = str(wednesday)[0:10]
        elif s[0] == "четверг":
            date = str(thursday)[0:10]
        elif s[0] == "пятница":
            date = str(friday)[0:10]
        elif s[0] == "суббота":
            date = str(saturday)[0:10]
        elif s[0] == "воскресенье":
            date = str(sunday)[0:10]
    else:
        if len(s) == 2 and (s[0] == "этот" or s[0] == "эта" or s[0] == "это" ):
            if s[1] == "понедельник":
                date = str(monday)[0:10]
            elif s[1] == "вторник":
                date = str(tuesday)[0:10]
            elif s[1] == "среда":
                date = str(wednesday)[0:10]
            elif s[1] == "четверг":
                date = str(thursday)[0:10]
            elif s[1] == "пятница":
                date = str(friday)[0:10]
            elif s[1] == "суббота":
                date = str(saturday)[0:10]
            elif s[1] == "воскресенье":
                date = str(sunday)[0:10]
        elif len(s) == 2 and (s[0] == "прошлый" or s[0] == "прошлая" or s[0] == "прошлое"):
            if s[1] == "понедельник":
                date = str(monday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "вторник":
                date = str(tuesday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "среда":
                date = str(wednesday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "четверг":
                date = str(thursday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "пятница":
                date = str(friday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "суббота":
                date = str(saturday - datetime.timedelta(days=7))[0:10]
            elif s[1] == "воскресенье":
                date = str(sunday - datetime.timedelta(days=7))[0:10]
        elif len(s) == 2 and (s[0] == "следующий" or s[0] == "следующая" or s[0] == "следующее"):
            if s[1] == "понедельник":
                date = str(monday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "вторник":
                date = str(tuesday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "среда":
                date = str(wednesday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "четверг":
                date = str(thursday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "пятница":
                date = str(friday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "суббота":
                date = str(saturday + datetime.timedelta(days=7))[0:10]
            elif s[1] == "воскресенье":
                date = str(sunday + datetime.timedelta(days=7))[0:10]
    date = date.split('-')
    date.reverse()
    date = '.'.join(date)
    return date


print(func1("32.02.2019"))
print(func2("завтра наступит, а 2010 уже не вернется"))
print (func3("следующий вторник"))

