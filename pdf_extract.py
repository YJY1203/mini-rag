from pypdf import PdfReader # PdfReader 클래스 임포트 (.pdf 파일을 객체로 파싱하는 작업을 수행 / 압축)

def extract_pages(path: str) -> list[dict]: # list[dict]은 타입 힌트, 어떻게 반환 타입을 정할지 미리 알 수 있다.
    """ 목표: PDF를 읽어 [{"page": 1, "text": ... }, ... ] 형태로 반환한다. """ # 목표 설정
    pages_list = [] # 리스트안에 dic을 설정할거라 먼저 빈 리스트 생성
    reader = PdfReader(path) # reader 안에 pdf파일 전체를 다루는 최상위 객체 생성후 참조 할당
    # PdfReader 클래스의 주요 속성:
    # reader.pages(페이지 목록), reader.metadata(제목·작성자), reader.is_encrypted(암호 여부)
    # reader.pages 에는 페이지 별로 가상 리스트를 만들어 리스트와 같은 역할 수행하고 직접 접근할때만 그에 맞는 요소를 반환 (지연 로딩)
    # 메모리에 객체의 모든 알맹이를 먼저 넣으면 오버플로우 발생할 수 있음

    for page_index, page in enumerate(reader.pages, start=1):
    # enumerate(순서가 있는 반복 데이터, 번호를 시작할 숫자 / 생략 시 기본값은 0)
    # 순서가 있는 데이터(리스트, 파일, reader.pages 등)를 반복문으로 돌릴 때,
    # 각 요소에 번호표를 자동으로 붙여 (번호, 요소) 형태의 튜플로 반환. (파이썬 내장 함수)

        pages_dic = {"page": page_index, "text": page.extract_text()}
        # {"page"(key: 번호(1)), "text"(reader.pages 첫 번째 요소의 문자를 반환)}
        # 모든 페이지를 순환하며 페이지별로 순서를 붙이고 순서별로 내용을 담음.

        pages_list.append(pages_dic) # dic 하나씩 리스트에 담음

    return pages_list # 리스트 반환

print(__name__) # 결과: __main__
# 파이썬은 .py 파일 하나를 읽어들일 때, 그 파일의 코드와 변수들을 담는 독립된 공간(모듈 객체)을 메모리에 만듭니다. 이때 우리가 직접 x = 10처럼 변수를 선언하지 않아도, 파이썬 엔진이 파일당 하나씩 몰래 만들어두는 기본 변수(내장 속성) 중 하나가 바로 __name__입니다.
# 직접 실행할 때 (python pdf_extract.py): 파이썬은 이 파일을 프로그램의 '시작점(주인공)'으로 인식하고, 이 파일 공간 안의 __name__ 변수에 "__main__"이라는 글자를 넣습니다.

# 왜 다른 파일에서 import하면 "pdf_extract"가 들어가나요?
# 이 코드가 저장된 원본 파일의 이름이 pdf_extract.py이기 때문.
# 다른 파일(예: main.py)에서 이 파일의 함수를 빌려 쓰기 위해 import pdf_extract라고 적으면, 파이썬은 다음과 같이 동작.
# 1. 주인공이 아님을 인식: main.py를 직접 실행했으므로 main.py의 __name__에는 "__main__"이 들어갑니다.
# 2. 부품(모듈) 이름 부여: 불려온 pdf_extract.py는 메인이 아니라 보조 부품으로 쓰이는 것이므로, 파이썬이 pdf_extract.py 공간의 __name__ 변수에 확장자(.py)를 뺀 실제 파일명("pdf_extract")을 자동으로 넣어줍니다. (만약 파일 이름이 my_tool.py였다면 __name__에는 "my_tool"이 들어갑니다.)

if __name__ == "__main__": # 이거는 자바의 static void main(){} 처럼 실행 메서드를 역할, 근데 파이썬은 위에서 아래로 한 줄씩 실행하기에, 자바처럼 JVM이 main메서드를 찾아 부르는게 아님
    pages = extract_pages("data/regulation.pdf") # 여기서 전에 작성한 extract_pages 함수 실행후 번호와 요소를 담은 리스트 반환 , path로는 "data/regulation.pdf"을 받아옴
    # ex)
    # pages = [
    #     {"page": 1, "text": "1쪽에서 추출한 글자 전체..."},   # pages[0]
    #     {"page": 2, "text": "2쪽에서 추출한 글자 전체..."},   # pages[1]
    #     {"page": 3, "text": "3쪽에서 추출한 글자 전체..."},   # pages[2]
    #     ...
    # ]

    # pages[2] → {"page": 3, "text": "..."} (dict 하나)
    # pages[2]["page"] → 3 (int)
    # pages[2]["text"] → "3쪽에서 추출한 글자 전체..." (str)

    print(f"총 {len(pages)}쪽")

    for p in pages[:3]: # 0부터 2까지 총 3번 수행,
        print(f"-- {p['page']}쪽 ({len(p['text'])}자)") # 리스트 0번 인덱스에서 1번(page), 1번 내용(text)가 들어 있고 dic은 [] 로 접근, 추가로 (f"...") 안에 표현식은 '' 로 작성하는게 가독성이 좋음.
        print(p['text'][:200])


    # PDF에서 추출한 날것의 텍스트(Raw Text)가 얼마나 지저분한지 눈으로 직접 확인하고,
    # 앞으로 어떤 전처리(청소) 작업을 해야 할지 파악하는 과정

    # 1, 2, 3쪽과 표가 있는 쪽(13, 14쪽)을 지정
    target_pages = [1, 2, 3, 13, 14]

    for p_num in target_pages:
        # pages 리스트는 0번 인덱스부터 시작하므로 p_num - 1을 사용
        text_content = pages[p_num - 1]["text"] # 해당 페이지의 text만 뽑기

        with open(f"data/raw_p{p_num}.txt", "w", encoding="utf-8") as f:
            f.write(text_content)



    # with open("파일경로", "모드", encoding="utf-8") as 별명: , with 블록(들여쓰기 된 부분)이 끝나면 에러가 나든 안 나든 파이썬이 알아서 f.close()를 호출

    # 파일 모드
    # 1. 기존 파일 접근 전용 모드 (파일경로에 파일이 없으면 에러 발생)
    # "r" (Read - 읽기 전용): 파일의 내용을 읽어오기만 할 때 씁니다. 모드를 생략하면 기본으로 "r"이 적용
    # "r+" (Read + Write - 읽기 및 쓰기): 기존 파일을 열어서 내용을 읽고, 원하는 위치에 덮어쓸 때 씁니다. (파일이 없으면 역시 에러가 납니다.)

    # 2. 새 파일 생성 가능 모드 (파일 경로에 파일이 없으면 자동으로 새로 만듦), 단, data/ 같은 상위 폴더 자체는 미리 존재해야 합니다.)
    # "w" (Write - 새로 쓰기 / 덮어쓰기)
    #   • 파일이 없으면: 새로 만듭니다.
    #   • 파일이 있으면: 기존 내용을 완전히 지우고 처음부터 새로 씁니다.

    # "a" (Append - 이어 쓰기)
    #   • 파일이 없으면: 새로 만듭니다.
    #   • 파일이 있으면: 기존 내용은 그대로 두고 파일의 맨 끝에 내용을 추가합니다.

    # "x" (Exclusive - 배타적 생성)
    #   • 파일이 없으면: 새로 만듭니다.
    #   • 파일이 있으면: 실수로 기존 파일(같은 이름의 파일)을 덮어쓰는 것을 막기 위해 에러(FileExistsError)를 발생시킵니다.

    # (참고: 위 모드들 뒤에 +를 붙이면("w+", "a+") 쓰면서 동시에 읽기도 가능해지고, b를 붙이면("rb", "wb") 텍스트가 아닌 이미지·PDF 같은 바이너리 데이터를 다룰 수 있습니다.)


    # 그렇게 생성한 raw_p{p_num}.txt
    # 표가 아니었던 텍스트들은 바닥글이 맨 위로 이동하거나 단어 중간 중간 강제로 줄바뀜이 생김
    # 왜? PDF 내부에 글자들이 저장된 순서(스트림 순서)의 기록의 차이와 원본 PDF의 오른쪽 여백(폭) 때문에 줄이 바뀐 곳마다 엔터(\n)가 그대로 들어가면서 멀쩡한 단어와 조사가 두 동강 났습니다.
    # 13,14쪽의 표 형태는 더 가관이다.
    # 표의 격자(행,열) 구조가 사라지고,칸 안의 글자들이 줄바꿈되거나 한 줄로 뒤섞여서 추출
    # 왜? PDF 파일은 엑셀이나 HTML처럼 '표(Table)'라는 구조 정보를 가지고 있지 않습니다. 단지 종이 위의 특정 좌표(x, y)에 글자와 선을 따로따로 그려놓은 그림에 가깝기 때문에, pypdf가 텍스트를 긁어올 때 칸 구분을 무시하고 좌표 순서대로 글자만 이어 붙여서 표 형태가 무너집니다.