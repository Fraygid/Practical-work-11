for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum ** 0.2)
                if e ** 5 == sum and e <= 150:
                    print(f'Сумма степеней равна: {a+b+c+d+e}')
                    exit()
