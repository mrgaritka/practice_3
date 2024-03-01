total_sec = int(input('Введите целое число от 1 до 86400: '))
hours = total_sec // 3600
minutes = (total_sec % 3600) // 60
sec = (total_sec % 3600) % 60
print(hours, ':', minutes, ':', sec)