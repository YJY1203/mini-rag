with open("memo.txt", encoding="utf-8") as f: # with open() 첨보지만 의미상 practice폴더 안 memo.text를 "utf-8"로 인코딩하고 그 객체를 f 별명을 붙인거 같은데?
    text = f.read() # 그럼 f(memo.txt)를 읽어들여서 text 객체에 담으라는거 같은데?
# f.read(): 파일의 처음부터 끝까지 모든 내용을 한 번에 쭉 읽어서, 하나의 거대한 문자열(str) 객체로 만들어 text 변수에 저장
# (참고: 이 줄이 끝나고 들여쓰기가 풀리는 순간, 위 with 문 덕분에 파일 f는 안전하게 닫힙니다. 하지만 이미 파일 내용을 text라는 문자열 변수에 복사해 두었기 때문에 아래 print()문에서 계속 사용할 수 있습니다.)

# 자바 대응 코드: String text = Files.readString(Path.of("practice/memo.txt"));

print(len(text)) # memo.txt의 문자열 길이(수) 반환
print(text) # memo.txt의 문자열 반환

# open(...): 하드디스크에 있는 memo.txt 파일을 프로그램으로 연결(스트림 개방)하는 함수
# encoding="utf-8": *"파일을 UTF-8로 인코딩한다"*기보다는, "이미 UTF-8 규칙으로 저장되어 있는 한글/텍스트 파일을 깨지지 않게 UTF-8 방식으로 해석해서 읽어와라"라는 뜻
# ( Python 3.14까지는 윈도우 기본 인코딩인 CP949와 충돌하여 한글이 깨지는 것을 막아줍니다.)
# with ... as f:: 열린 파일 연결 객체에 f라는 변수명을 붙이고, 블록(text = f.read())이 끝나는 순간 파이썬이 자동으로 f.close()를 호출해 파일을 닫아줍니다.(메모리 정리)

# 자바 대응 코드: try (BufferedReader f = Files.newBufferedReader(Path.of("practice/memo.txt"), StandardCharsets.UTF_8))

