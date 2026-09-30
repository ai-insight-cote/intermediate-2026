# 모험가 길드

def hero(leng: int, lis: list[int]):
    sort_list = sorted(lis) # 시간 복잡도 O(NlogN)
    people = 0
    count = 0
    # 1 2 2 2 3
    for value in (sort_list):
        # 일단 그룹에 사람을 넣어
        people += 1
        # 마지막으로 탐색된 사람이 그룹에서 제일 높은 공포도를 가지고 있음 왜냐? 공포도를 오름차순으로 정렬했기 때문에
        # 그 탐색된 사람의 공포도(value)가 명수(people)보다 크면 그룹 못함
        # 아니라면? 그룹 성공!(count+= 1) 다른 그룹 생성을 위해 people 초기화
        if(people >= value):
            count += 1
            people = 0 
    print(f"최대 그룹 : {count}")

if __name__ == '__main__':
    leng = int(input("모험가들이 몇 명인지 알려주세요 : "))
    inp = map(int, input("모험가들의 공포도를 입력하세요 : ").split())
    hero(leng, inp)