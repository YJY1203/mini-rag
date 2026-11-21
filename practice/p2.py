scores = [82,95,77]
# java라면 int[] scores = new int[]{82,95,77}; 라고 작성
# 그치만 파이썬은 [82,95,77]을 보고 배열 객체 scores를 생성?
# python의 list는 크기가 고정되는 자바의 배열보다는 크기가 유동적인 자바의 Array<integer>와 가까움
# List<Integer> list2 = new ArrayList<>(List.of(10, 20, 30)); // 자바 표현

for s in scores: # 자바라면 for(int i = 0; i < scores.length; i++) 또는 for(int s : scores)
    if s >= 90:
        print(s,"A")
    elif s >= 80: # elseif를 elif로 축약
        print(s,"B")
    else:
        print(s,"C")
# 조건식 뒤에 ':' 를 붙이고 줄바꿈하고 들여쓰기를 하여 조건식이 true일때 실행 본문을 구분지음
# scores에 담긴 순서대로(82,95,77) 점수 부여
for i in range(3): # rane(3)은 뭘 나타내는걸까? 범위 3?
# 0부터 시작해서 3개(끝값 직전까지만)의 연속된 정수(0, 1, 2)를 만들어내는 함수
# range(1, 4) → 1, 2, 3 (1부터 4 미만까지)
# range(0, 10, 2) → 0, 2, 4, 6, 8 (0부터 10 미만까지 2씩 증가)
# range(10, 0, -2)) → 10, 8, 6, 4, 2
    print(i)