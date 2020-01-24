# Github 설정

​	[Github 홈페이지](https://github.com/)



### 1. 초기 설정

- 초기화

> 처음 ***한 번*** 만
>
> 제일 ***최상단 디렉토리에서만***  할 것

```bash
$ git init
```

> 해당 디렉토리가 git 관리 아래에 들어감

- 계정 연결

```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL (master)
$ git config --global --list
fatal: unable to read config file (생략) # 아직 연결 안 된 상태

multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL (master)
$ git config --global user.name "github이름"

multicampus@DESKTOP-KVCQHCD MINGW64 ~/TIL (master)
$ git config --global user.email "github메일"
```

> 위에 적은 바와 같이 적어줄 것



### 2. github 연결

- remote를 이용해서 관리저장소에 연결해주어야 함

  ```bash
  $ git remote add origin url
  ```

  → **url** 부분에 본인이 연결할 **github의 Repository  주소**를 넣음

  → `add` 다음의 `origin` 은 `url`을 불러낼 `이름`으로 어떤 단어를 넣어도 상관없음

- 연결된 것 확인

  ```bash
  multicampus@DESKTOP-KVCQHCD MINGW64 ~/lectures (master)
  $ git remote -v
  origin url (fetch)
  origin url (push)
  ```

  → `별명` `url` 로 출력됨. 연결이 제대로 되었는 지 확인



- 연결을 잘못 했을 때

  ```bash
  $ git remote rm origin
  ```

  → `origin`은 본인이 위에서 본, 연결을 끊어야할 url의 `이름`을 적으면 됨
  
  ```bash
  $ git remote rename origin
  ```
  
  → `rename`으로 저장소의 `이름`을 바꿀 수 있다.



### 3. github에 올리기

- 상태 확인하기

  ```bash
    $ git status
  ```

  - add와 commit 전 후로 확인

  

- add

  ```bash
  $ git add 폴더/파일명		# 해당 폴더나 파일을 staging area로 올린다.
  
  $ git add .				   # 모든 변화를 staging area로 올린다.
  ```

- commit

  ```bash
  $ git commit -m "message"
  ```

  > commit 으로 add한 것을  snap shot을 찍는다.
  >
  > 추후 확인할 때 직관적으로 확인하기 위해 -m 으로 " " 안에  메시지를 남길 수 있다.

  - commit 한 log 확인하기

    ```bash
    $ git log
    ```

    > log 값이 모두 나온다.  `q`로 나올 수 있음

    ```bash 
    $ git log --pretty=oneline
    ```

    > log 값이 각각 한 줄로 나온다.



- push

  ```bash
  $ git push origin master
  ```

  → `origin` 이라는 이름을 붙여준  `url`을 부르고, `master` branch로 올린다.



### 4. github 가져오기

- 처음 **한 번만 clone** 만들기

  ```bash
  $ git clone url
  ```

  → 가져올 github의 repository의 url 주소를 복사해서 `url`에 넣는다.



- pull (항상 **시작**할 때마다 해줄 것)

  ```bash
  $ git pull origin master
  ```

  → `origin` 부분에는 가져올 github url의 `이름` 을 넣고 `master` branch에서 가져온다.



### 5. Github 계정 제거

- 제어판 - window 자격 증명 관리 - github 계정 제거

  ![github_delect](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FHs4T3%2FbtqBqjc1zJ3%2F0a4omwWiL4chMHvjDXT3dK%2Fimg.png)



### 6. 기타

- 디렉토리 이동

  ```bash
  $ cd 이동할디렉토리
  ```

  (+) 상위 디렉토리로 이동하고 싶으면

  ```bash
  $ cd ..
  ```

- 목록 리스트

  ```bash
  $ ls
  $ ls -a			## 해당 디렉토리의 전체 목록
  ```

- 디렉토리 생성

  ```bash
  $ mkdir 폴더명
  ```

- 파일 생성

  ```bash
  $ touch 파일명.파일확장자
  ```

- .gitignore

  ```bash
  $ touch .gitignore
  ```

  > .gitigrnore 파일 안에 파일명.확장자로 적어둔 파일은 git의 트래킹을 피할 수 있다.