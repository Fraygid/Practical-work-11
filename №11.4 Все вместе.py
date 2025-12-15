num = int(input('Введите натуральное число: '))
num_ = num
cnt_3 = cnt_last = cnt_even = sum_5 = cnt_0_5 = 0
last_digit = num % 10
sum_7 = 1

while num > 0:
    last_num = num % 10

    if last_num == 3:
        cnt_3 += 1
    if last_num == last_digit:
        cnt_last += 1
    if last_num % 2 == 0:
        cnt_even += 1
    if last_num > 5:
        sum_5 += last_num
    if last_num > 7:
        sum_7 *= last_num
    if last_num == 0 or last_num == 5:
        cnt_0_5 += 1

    num = num // 10

print(f'Кол-во цифр 3: {cnt_3}')
print(f'Сколько раз встречается последняя цифра: {cnt_last}')
print(f'Кол-во четных цифр: {cnt_even}')
print(f'Сумма цифр, больших 5: {sum_5}')
print(f'Произведение цифр, больших семи: {sum_7}')
print(f'Сколько раз встречаются 0 и 5 суммарно: {cnt_0_5}')
