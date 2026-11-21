s = "  Hello, World! Hello!  "

print(s.strip())  # 예상 결과:Hello, World! Hello!(양쪽 공백 제거?)
print(s.lower())  # 예상 결과:  hello, world! hello!  (근데 "  Hello, World! Hello!  "의 객체가 print()문을 거치면서 형태가 원본으로 유지되는건가? 아님 메서드에 의해서 계속해서 변하는건가?
print(s.replace("Hello", "Bye")) #예상 결과:  Bye, World! Bye!
print(s.split()) # 이거 무슨 메세드인지 모르겠네? 분열?
print("world!".strip("!")) # 이것도 모르겠음

# 자바의 String이 불변(Immutable) 객체인 것처럼, 파이썬의 문자열(str)도 불변 객체
# 메서드 수행: 완전히 새로운 문자열 객체를 하나 더 만들어서 반환

# strip(): 문자열 양쪽 끝에 있는 불필요한 공백(띄어쓰기, 줄바꿈 등)을 잘라낸 새 문자열을 반환
# 자바 대응: s.trim() 또는 s.strip()과 똑같습니다.

# python: s.lower() / java:	s.toLowerCase()	, 소문자로 변환

# python: s.replace("A", "B") / java: s.replace("A", "B"), 문자열 치환

# s.split() → 출력: ['Hello,', 'World!', 'Hello!'] (리스트 반환)
# 문자열을 공백(띄어쓰기) 기준으로 쪼개서 리스트([])에 담아 반환
# 자바 대응: s.split(" ")을 호출해 String[] 배열로 돌려받는 것과 같습니다.

# "world!".strip("!") → 출력: "world" (양쪽 끝의 특정 문자 제거)
# strip() 괄호 안에 아무것도 안 넣으면 양쪽 공백을 지우지만, 특정 문자를 넣으면 양쪽 끝에서 그 문자를 찾아 지워줍니다