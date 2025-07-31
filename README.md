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
- `1516`, `3733` python으로 풀면 시간초과 -> pypy로 풀기
- `3704` 재귀 깊이 한계 때문에 다음과 같은 구문을 추가해주어야 함:
```
import sys
sys.setrecursionlimit(10**6) # 대충 큰 수
```

### BOJ
- `2805` 이분탐색 써도 pypy3로 풀어야 함

## C언어로 풀어야 하는 문제들
- `1430`, `3014`
