def steps(number):
    curentValue = number;
    steps = 0;

    while curentValue != 1:
        if curentValue <= 0:
            raise ValueError("Only positive integers are allowed")
        if curentValue % 2 == 0:
            curentValue = curentValue // 2
        else:
            curentValue = 3 * curentValue + 1
        steps += 1

    return steps
