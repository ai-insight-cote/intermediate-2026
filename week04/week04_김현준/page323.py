def StringCompression(s: str):
    """
    ==========================================================================================
    문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을,
    **문자열 압축 알고리즘**이라고 합니다.
    
    압축할 문자열 s가 매개변수로 주어질 때，위에 설명한 방법으로 1 개 이상 단위로 문자열을 잘라 압축하여 
    표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

    💙예시 
    | 입력 (s) | 가장 짧은 압축문자열 | 출력 (return) |
    | :--- | :--- | :--- |
    | "aabbaccc" | "2a2ba3c" | 7 |
    | "ababcdcdababcdcd" | "2ababcdcd" | 9 |
    | "abcabcdede" | "2abcdede" | 8 |
    | "abcabcabcabcdededededede" | "2abcabc2dedede" | 14 |
    | "xababcdcdababcdcd" |  "(압축 불가능)" | 17 | 

    ❌제한사항
     • s의 길이는 1 이상 1,000 이하입니다.
     • s는 알파벳 소문자로만 이루어져 있습니다.

    ==========================================================================================
    """

    min_num = 1001
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
    # 길이가 1일때 1 길이로 배열 만들기
        start = 0
        arr = []
        while start < len(s):
            window_str = s[start : start+i]
            arr.append(window_str)
            start += i

        # 압축해보자.
        # part1 은 앞에 있는 문자, part2 은 뒤에 온 문자. 이 둘을 비교한다.
        # part1 == part2처럼, 비교연산자를 통해 연속인지 아닌지 판별한다.
        part1 = arr[0]
        count = 1
        result = ""
        for index in range(1, len(arr)):
            part2 = arr[index]
            # 연속으로 나와서, 압축이 가능하다면
            if part1 == part2:
                # 카운트로 넘어가서, 압축했다고 넘어가기.
                count += 1
            # 연속이 아니라서, 압축이 불가능하다면
            else:
                # 그동안의 저장한 압축 붙이기
                # 한개 연속이라면, 그냥 나열
                if count == 1:
                    result += part1
                # 그 이상 개수 연속이라면, 개수를 결과값에 추가하며 나열
                else:
                    result += str(count)
                    result += part1
                # 카운트 다시 세기 (초기화 1)
                count = 1
            part1 = part2

        if count == 1:
            result += part1
        # 그 이상 개수 연속이라면, 개수를 결과값에 추가하며 나열
        else:
            result += str(count)
            result += part1
        # 카운트 다시 세기 (초기화 1)
        min_num = min(len(result), min_num)

    return min_num


print(StringCompression("a"))