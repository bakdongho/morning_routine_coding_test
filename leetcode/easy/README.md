# Leet code Easy

### 14. Longest Common Prefix

* 문제 설명

1. 입력 데이터: string list
2. 모든 string 중에서 시작단어가 겹치는게 있으면 그 값을 return
3. 겹치는게 없다면 empty string("") return

* 조건

1. list 길이는 200을 넘지 않음.
2. string의 길이도 200을 넘지 않음.
3. string은 소문자 영어이다.

* [풀이](src/longest_common_prefix.py)

* 실수한 점

1. 처음 로직 짤 때 실패에 대한 처리만 했지, 성공에 대한 로직을 짜지 않아서 예외케이스(같은 string만 있을때, 하나의 string만 있을 때)를 고려하지 못함.