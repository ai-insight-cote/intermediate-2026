def mul_or_plus(st: str):
    answer = int(st[0])
    for ch in st[1:]:
        num = int(ch)
        if answer <= 1 or num <= 1:
            answer = answer + num
        else:
            answer = answer * num
    print(answer)


if __name__ == "__main__":
    mul_or_plus(input("숫자를 입력하세요:"))