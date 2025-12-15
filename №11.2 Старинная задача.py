print('У вас есть 100 руб. Вы можете на них купить:')

for bull in range(11):
    for cow in range(21):
        for calf in range(201):
            if bull * 10 + cow * 5 + calf * 0.5 == 100:
                print(f'быков={bull}, коров={cow}, телят={calf}')
