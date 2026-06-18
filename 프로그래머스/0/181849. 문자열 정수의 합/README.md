# [level 0] 문자열 정수의 합 - 181849 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181849?language=python3) 

### 성능 요약

메모리: 11.5 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 06월 18일 15:34:18

### 문제 설명

<p>한 자리 정수로 이루어진 문자열 <code>num_str</code>이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>num_str</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_str</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"123456789"</td>
<td>45</td>
</tr>
<tr>
<td>"1000000"</td>
<td>1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>문자열 안의 모든 숫자를 더하면 45가 됩니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>문자열 안의 모든 숫자를 더하면 1이 됩니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

### 문제 풀이 정리

1. 입력: 문자열 num_str(한 자리 정수) - 3 <= num_str <= 100
2. 출력: 각 자리수의 합 result
3. 입출력 예: 

| num_str | result |
|---|---|
| "123456789" | 45 |
| "1000000" | 1 |

4. 핵심 동작: 문자열을 for문으로 하나씩 순회하면서 int형으로 변환 후 다 더하기
5. 필요한 도구:
   - for 반복문, int()
6. 로직 3줄:
   - 문자열 for 반복문 순회
   - 한 문자씩 int로 변환 후 answer에 더함
   - answer 반환
7. 오답 노트
   - 기존 풀이 문제점 : 리스트로 변환 후 순회하려다가 answer += num_list[i-1] 같은 리스트 안의 값을 인덱스로 사용하려고 함
