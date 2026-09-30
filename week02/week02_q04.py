def min_coin(N: int, coin_list: list[int]):
    coinlist = sorted(coin_list)
    max = sum(coinlist)
    avail_set = {0}
    for coin in coinlist:
        temp_list = list(avail_set)
        for avail in temp_list:
            avail2 = avail + coin
            avail_set.add(avail2)

    for min_coin in range(1, max + 2):
        if min_coin not in avail_set:
            print(min_coin)
            return



if __name__ == "__main__":
    N = int(input("동전 개수를 입력하세요 : "))
    coin_list = map(int, input("동전들의 값들을 입력하세요(공백 구분): ").split())
    min_coin(N, coin_list)