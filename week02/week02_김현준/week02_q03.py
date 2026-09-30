def slap(st: str):
    count = 0
    a = st[0]
    for b in st[1:]:
        if b != a:
            count += 1
        a = b
    print(count // 2 + count % 2)

if __name__ == "__main__":
    slap(input("숫자를 입력하세요:"))