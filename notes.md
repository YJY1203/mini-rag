# Mini-RAG 트러블슈팅 노트
## 2026-11-16 GitHub 첫 push 시 GH007 이메일 비공개 제한 에러
- 증상: `git push -u origin main` 실행 시 `push declined due to email privacy restrictions` 에러 발생
- 원인: GitHub 계정의 이메일 비공개 보호 설정이 켜져 있는데, 로컬 Git `user.email`에 실제 개인 이메일을 등록해 커밋함
- 해결: GitHub Settings에서 `@users.noreply.github.com` 주소를 확인해 `git config`를 변경하고, `git commit --amend --reset-author --no-edit`로 기존 커밋 작성자 정보를 갱신 후 재전송함


## 2026-11-20 pdf_extract.py 예측 후 실행 (잘못된 인자 넣어보기)

### 1) extract_pages(123): 숫자를 넣은 경우
- 예측: IntelliJ가 `123`에 타입 경고 밑줄 → 실행하면 에러
- 증상: IDE 경고(str 자리에 int)는 떴지만 실행은 됨 → `AttributeError: 'int' object has no attribute 'seek'`
- 위치: `pdf_extract.py` 6번째 줄 `reader = PdfReader(path)` → pypdf 내부 `stream.seek(0)`
- 원인: PdfReader는 문자열이면 "파일 경로"로 보고 직접 열고, 문자열이 아니면 "이미 열린 파일 객체"라고 믿고 검사 없이 파일처럼 다룸(덕 타이핑). 123에게 `seek(0)`(맨 앞으로 되감기)을 시켰는데 int 객체에는 그 메서드가 없어서 실패. 123이라는 파일이 있는 게 아님
- 배운 점: 타입 힌트는 메모일 뿐 실행을 막지 않음. 잘못된 값은 엉뚱한 곳에서 엉뚱한 이름의 에러로 터질 수 있으니 IDE 경고를 무시하지 말 것

### 2) extract_pages("data/없는파일.pdf"): 없는 파일을 넣은 경우
- 예측: 경고는 없고, 실행하면 파일 관련 에러
- 증상: IDE 경고 없음 → `FileNotFoundError: [Errno 2] No such file or directory`
- 위치: 같은 6번째 줄 → pypdf 내부 `open(stream, "rb")`
- 원인: 타입(str)은 맞지만 파일 존재 여부는 실행해야 알 수 있음
- 배운 점: PdfReader는 생성되는 순간 파일 전체를 메모리로 읽음 (미뤄지는 건 페이지 "해석"뿐 = 지연 파싱)

### 3) KeyError: 'page'
- 증상: 출력 부분에서 `KeyError: 'page'` 발생
- 원인: 저장할 때 키는 `"pages"`, 꺼낼 때는 `'page'`로 철자가 다름
- 해결: 저장·조회 키를 `"page"`로 통일. dict 키는 한 글자만 달라도 다른 키

### 트레이스백 읽는 법
- 맨 아래 줄 = 에러 이름과 이유
- 위 → 아래 = 호출 순서 (바깥 → 안쪽). 자바 스택 트레이스와 방향이 반대
- 내 파일 이름이 나오는 마지막 줄 = 내가 고칠 곳. `site-packages/...`는 라이브러리 내부

## 2026-11-23 덕 타이핑과 seek (실험 1에서 파생)
- 파이썬은 숫자도 객체(123 = int 객체). 다만 객체마다 가진 메서드가 다름. `seek()`는 파일 종류의 객체에만 있음
- 덕 타이핑: 타입을 미리 검사하지 않고 "그렇게 쓸 수 있겠지" 하고 일단 써 봄 → 안 되면 그때 에러. 자바는 매개변수 타입이 안 맞으면 컴파일 단계에서 막힘
- 파일 객체에는 "어디까지 읽었는지" 표시하는 커서(책갈피)가 있음. `read()`하면 뒤로 밀리고, `seek(위치)`로 원하는 곳에 옮김
- PdfReader가 처음에 `seek(0)` 하는 이유: 남이 준 파일은 커서가 중간에 있을 수 있어서 맨 앞으로 되돌리고 시작
- PDF에 seek가 꼭 필요한 이유: 앞(%PDF- 확인) → 맨 뒤(XRef 목차) → 목차가 가리키는 위치로 점프하며 읽는 구조라서. 자바의 `RandomAccessFile.seek()`과 같은 역할

## 2026-11-20 pdf_extract.py 핵심 개념 요약
- 결과 리스트는 반복문 밖에서 한 번, 페이지별 dict는 반복문 안에서 매번 새로 (밖에서 만들면 같은 dict를 덮어씀)
- 리스트는 위치(0, 1, 2)로, dict는 키 이름으로 꺼냄
- 구조: reader(PdfReader) → reader.pages(가상 리스트 하나) → page(PageObject)
- page는 글자가 아니라 글꼴·위치·그리기 정보 덩어리 → 글자는 `extract_text()`로 꺼냄
- `enumerate(..., start=1)`: (번호, 요소) 묶음을 건네주고 for 문이 두 변수로 언패킹
- `a or b`: a가 비어 있으면 b를 돌려줌 (자바 `||`와 달리 값 자체를 반환)
- 타입 힌트(`path: str`, `-> list[dict]`): 사람과 IDE를 위한 메모. 실행할 때 검사하지 않음
- `__name__`: 직접 실행하면 "__main__", import되면 파일 이름. import할 때도 파일 전체가 실행되므로 테스트 코드는 `if __name__ == "__main__":` 아래에
- f-string 안의 키는 바깥과 다른 따옴표로 (`f"{p['page']}"`), Python 3.11까지는 같은 따옴표를 쓰면 문법 오류