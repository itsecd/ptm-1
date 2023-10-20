def luna(number: str) -> str:
    temp = 0
    for i in range(len(number)):
        if i % 2 != 1:
            tmp = int(number[i]) * 2
            if tmp > 9:
                temp += tmp - 9
            else:
                temp += tmp
        else:
            temp += int(number[i])
    #print(number)
    if temp % 10 == 0:
        print("Последовательность верна")
        return True
    else:
        print("Последовательность не верна")
        return False
