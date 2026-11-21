stock = {"apple": 3, "banana": 5}
# 파이썬에서 {} 표현? 뭘 뜻하는거지? 문자열뒤에 : 3 ? 이건또 무슨 표현이지?
# Map<String, Integer> stock = new HashMap<>(); (자바의 HashMap과 완전히 똑같은 자료구조)
# stock.put("apple", 3);
# stock.put("banana",5); // 자바에서는 하나씩 만들어줘야 함.

# 딕셔너리 생성 ({} 와 : 의 의미)
# {} (중괄호): 자바에서 new HashMap<>()을 선언하는 것과 같습니다. 키(Key)와 값(Value)을 짝지어서 저장하는 공간을 만듭니다.

stock["cherry"] = 7 # stock 딕셔너리에 cherry(key)의 7(값) 추가
stock["apple"] = stock["apple"] + 1 # 기존 apple(key)의 값 3을 꺼내서 1을 더한뒤 덮어씀, 즉 "apple"의 값은 4가 됨.

print(stock["apple"]) # "apple"을 꺼내서 값 4를 출력
print("grape" in stock) # stock dic에서 "grape"가 있는 확인, 없으므로 False 출력
print(stock.get("grape",0)) # "grape"의 값을 찾되, 만약 키가 없으면 기본값인 0을 반환
# print(stock["grape"]) # 대괄호 []로 없는 키를 직접 조회하면 KeyError라는 예외(Exception)가 발생하며 프로그램이 강제 종료

for fruit, count in stock.items(): # 딕셔너리에 들어있는 모든 키와 값을 한 쌍씩 꺼내 반복
    print(fruit, count)
