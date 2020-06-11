# github으로 협업하기

1. repository를 새로 만든다.
2. collaborator를 추가한다.
3. 상대방 승인을 기다린다.

---

__무조건 master branch로 이동하여 pull한 후 수정해야함__

- git branch 과정

  ```
  1. 구현해야 하는 기능 별로 브랜치를 생성한다.
  2. 생성한 브랜치 내에서 진행한 작업들을 Commit한다.
  3. 로컬에서만 작업하면 다른분들과 공유가 안되니 원격 저장소에 Push한다. (최소 하루에 한번은 내 작업을 커밋, 푸시한다)
  4. 기능구현이 완료 되면 마스터 브랜치에 Merge Request를 보낸다.
  5. 동료분의 코드 리뷰가 끝나고 이상이 없으면 마스터 브랜치에 내 작업물이 Merge 된다.
  ```

  ```
  1. git checkout -b brchY
  브랜치를 생성하고 해당 브랜치로 이동할거에요. 이 브랜치는 Y의 브랜치입니다.
  2. git add .
  모든 변경사항을 tracking 되는 상태로 변경할거에요.
  3. git commit -m “Add Input Form for Login”
  이번 작업은 로그인을 위한 폼을 만든 거에요. 커밋 할게요!
  3-1. git push --set-upstream origin brchY
  내가 작업하고 있는 브랜치를 동료들도 볼 수 있게 원격에 올릴게요
  
  4. push하면 gitlab/github에 Pull Request나 Merge Request 생성하는 버튼이 활성화
  5. (메신저로) @동료님 저 이번에 로그인 페이지 작업했고 해당 작업 사항 MR(PR) 올렸습니다! 피드백 부탁드립니다! 감사합니다~
  ```
---

