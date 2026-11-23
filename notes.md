# Mini-RAG 트러블슈팅 노트
## 2026-11-16 GitHub 첫 push 시 GH007 이메일 비공개 제한 에러
- 증상: `git push -u origin main` 실행 시 `push declined due to email privacy restrictions` 에러 발생
- 원인: GitHub 계정의 이메일 비공개 보호 설정이 켜져 있는데, 로컬 Git `user.email`에 실제 개인 이메일을 등록해 커밋함
- 해결: GitHub Settings에서 `@users.noreply.github.com` 주소를 확인해 `git config`를 변경하고, `git commit --amend --reset-author --no-edit`로 기존 커밋 작성자 정보를 갱신 후 재전송함

