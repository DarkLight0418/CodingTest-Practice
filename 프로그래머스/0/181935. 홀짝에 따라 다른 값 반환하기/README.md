# [level 0] 홀짝에 따라 다른 값 반환하기 - 181935 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181935?language=python3) 

### 성능 요약

메모리: 11.4 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 07월 03일 10:10:52

### 문제 설명

<p>양의 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 홀수라면 <code>n</code> 이하의 홀수인 모든 양의 정수의 합을 return 하고 <code>n</code>이 짝수라면 <code>n</code> 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
<td>16</td>
</tr>
<tr>
<td>10</td>
<td>220</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>n</code>은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>n</code>은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 2<sup>2</sup> + 4<sup>2</sup> + 6<sup>2</sup> + 8<sup>2</sup> + 10<sup>2</sup> = 4 + 16 + 36 + 64 + 100 = 220을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

### [문제 풀이 체크리스트]

1. 입력: 양의 정수 n
2. 출력: n이 홀수 : n 이하의 홀수인 모든 양의 정수의 '합'
	  n이 짝수 : n 이하의 짝수인 모든 양의 정수의 '제곱의 합'
3. 예시 변환: n == 7 -> result == 16 / n == 10 -> result == 220
4. 핵심 동작: 조건문을 통해 홀수와 짝수를 구분하고, 그에 따라 계산 방식을 분류하여 작성
5. 필요한 도구:
    - 조건문 (if / elif)
    - 반복문 (for)
    - 누적 변수 (sum)
6. 의사코드: 
	- n을 받으면 if else문에 따라 값을 판단
	- 홀수일 경우 n 이하의 홀수 정수의 합 반환
	- 짝수일 경우 n 이하의 짝수 정수의 제곱의 합 반환

