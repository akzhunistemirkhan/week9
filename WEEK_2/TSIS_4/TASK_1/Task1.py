import re
file = open(r'text.txt', 'r', encoding = 'utf-8')
data = file.read()

name = re.compile(r'Филиал\sТОО\s\w+\s\w+')
Bin = re.compile(r'\d{12}')
titles = re.compile(r'\d+\.\n(.*)')
count = re.compile(r'(\d),\d{3}')
price = re.compile(r'x\s([\d\s]+,\d+)')
Total = re.compile(r'Стоимость\n([\d\s]+\,\d+)')
Date = re.compile(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}')
address = re.compile(r'г\.\s[\w\-]+\,\w+\,\s[\w\s]+\,\d+\,\s\w+\-\d')

Name = re.search(name, data)
BIN = re.search(Bin, data)
Date = re.search(Date, data)
Address = re.search(address, data)
Titles = re.findall(titles, data)
Count = re.findall(count, data)
Prices = re.findall(price, data)
total = re.findall(Total, data)

print(Name.group(0))
print('БИН',BIN.group(0))
print('Кассир Аптека 17-1')
print('ПРОДАЖА')
for i in range(len(Titles)):
    print(Titles[i])
    print(Count[i],'x',Prices[i])
    print(Prices[i])
    print('Стоимость')
    print(total[i])
print('Время:' + Date.group(0))
print(Address.group(0))