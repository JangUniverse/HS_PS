# HS_PS
- 한성과학고등학교에서 진행하는 알고리즘 챌린지 대비 문제 연습장
- 일단 `python`, 안되면 `pypy`(문법은 같음), 이것도 안되면 gpt한테 `C++`로 해 달라고 하기
- 링크: [개념서처럼 정리해놓은 유형](https://00ad-8e71-00ff-055d.tistory.com/), [쉽게 보기 좋은 유형](https://blog.naver.com/kks227)
   
### JangUniverse
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=janguniverse)](https://solved.ac/profile/janguniverse)
[![mazandi profile](http://mazandi.herokuapp.com/api?handle=janguniverse&theme=dark)](https://solved.ac/profile/janguniverse)

### slsl 
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=djsiui12)](https://solved.ac/profile/djsiui12)
[![mazandi profile](http://mazandi.herokuapp.com/api?handle=djsiui12&theme=dark)](https://solved.ac/profile/djsiui12)

## 명명법
- 기본적으로 CodeUp 문제 숫자를 이용
- 단, 생각이 오래 걸린 문제인 경우 `thinked`, gpt 쓴 경우 `gpt`, 못 푼 문제인경우 `unsoloved` 사용.
- 알파벳순으로 입력할 것.
- 승후 화이팅


## 특이한 문제들
### CodeUp
- ~~`1516`, `3733` python으로 풀면 시간초과 -> pypy로 풀기~~ --> 걍 알고리즘에 백트래킹 있으면 무조건 pypy로 풀어
- `3704` 재귀 깊이 한계 때문에 다음과 같은 구문을 추가해주어야 함:
```
import sys
sys.setrecursionlimit(10**6) # 대충 큰 수
```

### BOJ
- `2805`, `2473`, `11049` 이분탐색 써도 pypy3로 풀어야 함

## C언어로 풀어야 하는 문제들
- `1430`, `3014`

# 처음보는 문법
## lambda
`sort(lambda)`는 `lambda` 다음에 오는 매개변수를 기준으로 정렬하는 문법임.  
ex. `li.sort(key = lambda x: x[0])`이면 `x[0]`을 기준으로 정렬, `li.sort(key = lambda x: (x[1], x[0]))`이면 x[1]로 정렬하다가 같은 값을 만났을 경우에 x[0]에 대해서 정리하는 거  
--> 도서관 정렬과 비슷함.

# Python 언어 문제 풀 때 팁  
python 언어가 PS 할 때 너무 쓰레기이므로, 이런 스킬을 써야 함.

## import 적극 활용
```
import sys  
input = sys.stdin.readline
```
개행 문자 입력 받는 코드, 단점은 ``Hello, world!``를 입력받으면 ``Hello, world!\n``으로 들어옴.  

--> int 받을 때 주로 쓰면 됨  
``sys.setrecursionlimit(10**6)``
재귀 호출 횟수 늘리기  

``from collections import deque``
덱 만들기 --> 구현한 queue보다 빠름

``from bisect import bisect_left``  
이분 탐색 알고리즘 구현하기 편함 

``import heapq``  
우선순위 큐 구현하기 편함 