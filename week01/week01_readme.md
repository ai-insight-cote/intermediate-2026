# Greedy Algorithm Practice

그리디 알고리즘 기본 문제 풀이 정리입니다.

## 목차

1. [큰 수의 법칙](#1-큰-수의-법칙)
2. [숫자 카드 게임](#2-숫자-카드-게임)
3. [1이 될 때까지](#3-1이-될-때까지)

---

# 1. 큰 수의 법칙

주어진 수들을 `M`번 더하여 가장 큰 수를 만드는 문제이다.

단, 배열의 특정 인덱스에 해당하는 수가 **연속해서 `K`번을 초과하여 더해질 수 없다.**

### 예시

```text
배열 = [2, 4, 5, 4, 6]

M = 8
K = 3
```

가장 큰 수인 `6`을 최대 `K = 3`번까지 연속해서 더할 수 있다.

```text
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46
```

---

## 문제

### 입력 조건

- 첫째 줄에 `N`, `M`, `K`의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
  - `2 ≤ N ≤ 1,000`
  - `1 ≤ M ≤ 10,000`
  - `1 ≤ K ≤ 10,000`

- 둘째 줄에 `N`개의 자연수가 공백으로 구분되어 주어진다.
- 각각의 자연수는 `1 이상 10,000 이하`이다.
- 입력으로 주어지는 `K`는 항상 `M`보다 작거나 같다.

### 출력 조건

- 큰 수의 법칙에 따라 더한 결과를 출력한다.

### 입력 예시

```text
5 8 3
2 4 5 4 6
```

### 출력 예시

```text
46
```

---

## 작성 코드

```python
# N, M, K 입력 받기
N, M, K = map(int, input().split())

# N개의 자연수 입력
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

# 가장 큰 수와 두 번째로 큰 수
first_num = data[-1]
second_num = data[-2]

i = 0
flag = 0
result = 0

while i < M:
    i += 1

    if flag < K:
        result += first_num
        flag += 1
    else:
        result += second_num
        flag = 0

print(result)
```

### 풀이 아이디어

가장 큰 수를 `K`번 더한 뒤 두 번째로 큰 수를 한 번 더한다.

이 과정을 총 `M`번의 덧셈이 수행될 때까지 반복한다.

```text
6 6 6 5 | 6 6 6 5
```

---

## 반복문을 이용한 풀이

```python
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    # 가장 큰 수를 K번 더하기
    for _ in range(k):
        if m == 0:
            break

        result += first
        m -= 1

    if m == 0:
        break

    # 두 번째로 큰 수를 한 번 더하기
    result += second
    m -= 1

print(result)
```

---

## 수학적 아이디어

다음과 같은 수열이 반복된다.

```text
6, 6, 6, 5
```

반복되는 수열의 길이는

```text
K + 1
```

전체 `M`번의 덧셈 중 완전한 수열이 반복되는 횟수는

```text
M // (K + 1)
```

따라서 가장 큰 수의 등장 횟수는 다음과 같다.

```text
(M // (K + 1)) × K
```

여기에 나머지 부분에서 등장하는 가장 큰 수의 횟수를 더한다.

```text
(M // (K + 1)) × K + M % (K + 1)
```

### 수학적 풀이 코드

```python
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0

result += count * first
result += (m - count) * second

print(result)
```

---

# 2. 숫자 카드 게임

숫자 카드 게임은 여러 개의 숫자 카드 중에서 게임의 규칙에 맞게 **가장 높은 숫자의 카드 한 장을 선택하는 문제**이다.

## 게임 규칙

1. 숫자가 쓰인 카드가 `N × M` 형태로 놓여 있다.
   - `N`: 행의 개수
   - `M`: 열의 개수

2. 먼저 카드를 뽑을 행 하나를 선택한다.
3. 선택한 행에서 **가장 숫자가 낮은 카드**를 뽑아야 한다.
4. 따라서 각 행의 최솟값을 확인한 뒤, 그중 가장 큰 값을 선택해야 한다.

즉,

```text
각 행의 최솟값 → 그 값들 중 최댓값
```

을 찾는 문제이다.

---

## 문제

### 입력 조건

- 첫째 줄에 행의 개수 `N`과 열의 개수 `M`이 공백으로 구분되어 주어진다.
  - `1 ≤ N, M ≤ 100`

- 이후 `N`개의 줄에 걸쳐 카드에 적힌 숫자가 주어진다.
- 각 숫자는 `1 이상 10,000 이하`의 자연수이다.

### 출력 조건

- 게임의 규칙에 따라 선택할 수 있는 카드의 숫자를 출력한다.

### 입력 예시 1

```text
3 3
3 1 2
4 1 4
2 2 2
```

### 출력 예시 1

```text
2
```

### 입력 예시 2

```text
2 4
7 3 1 8
3 3 3 4
```

### 출력 예시 2

```text
3
```

---

## 작성 코드

```python
# N, M 입력 받기
N, M = map(int, input().split())

result = float('-inf')

for _ in range(N):
    data = list(map(int, input().split()))

    if result <= min(data):
        result = min(data)

print(result)
```

### 풀이 아이디어

각 행에서 가장 작은 값을 구한다.

```text
3 1 2 → 1
4 1 4 → 1
2 2 2 → 2
```

그 후 각 행의 최솟값 중 가장 큰 값을 선택한다.

```text
max(1, 1, 2) = 2
```

즉,

```text
max(min(각 행))
```

의 구조이다.

---

## `min()`, `max()`를 이용한 풀이

```python
n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)
    result = max(result, min_value)

print(result)
```

---

## 2중 반복문을 이용한 풀이

```python
n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))

    # 현재 행에서 가장 작은 수 찾기
    min_value = 10001

    for value in data:
        min_value = min(min_value, value)

    # 각 행의 최솟값 중 가장 큰 값 찾기
    result = max(result, min_value)

print(result)
```

---

# 3. 1이 될 때까지

어떤 수 `N`이 `1`이 될 때까지 다음 두 연산 중 하나를 반복해서 수행한다.

1. `N`에서 `1`을 뺀다.
2. `N`을 `K`로 나눈다.

단, **두 번째 연산은 `N`이 `K`로 나누어떨어질 때만 사용할 수 있다.**

목표는 `N`을 `1`로 만드는 **최소 연산 횟수**를 구하는 것이다.

---

## 문제

### 입력 조건

- 첫째 줄에 `N`과 `K`가 공백으로 구분되어 주어진다.
  - `2 ≤ N ≤ 100,000`
  - `2 ≤ K ≤ 100,000`

- `N`은 항상 `K`보다 크거나 같다.

### 출력 조건

- `N`이 `1`이 될 때까지 필요한 최소 연산 횟수를 출력한다.

### 입력 예시

```text
25 5
```

### 출력 예시

```text
2
```

---

## 작성 코드

```python
# N, K 입력 받기
N, K = map(int, input().split())

count = 0

while N > 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1

    count += 1

print(count)
```

### 풀이 아이디어

`N`이 `K`로 나누어떨어진다면 `1`을 빼는 것보다 나누는 것이 숫자를 훨씬 빠르게 줄일 수 있다.

따라서 다음 전략을 사용한다.

```text
N % K == 0
    → K로 나누기

N % K != 0
    → 1 빼기
```

예를 들어,

```text
N = 25
K = 5
```

이라면

```text
25 → 5 → 1
```

총 `2번`의 연산만으로 `1`을 만들 수 있다.

---

# 핵심 정리

| 문제           | 핵심 전략                                               |
| -------------- | ------------------------------------------------------- |
| 큰 수의 법칙   | 가장 큰 수를 `K`번 더한 후 두 번째 큰 수를 한 번 더하기 |
| 숫자 카드 게임 | 각 행의 최솟값 중 최댓값 선택                           |
| 1이 될 때까지  | `K`로 나누어떨어지면 나누고, 아니면 `1` 빼기            |

세 문제 모두 현재 상황에서 가장 유리한 선택을 반복하는 **Greedy Algorithm**의 기본 문제이다.
