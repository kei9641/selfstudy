# Jupyter 설정

### 1. 설치

```bash
$ pip install jupyter
```



### 2. 실행

```bash
$ jupyter notebook
```

- 좀 더 짧게 써서 켜보기

  ```bash
  $ code ~/.bashrc
  ```

  → 실행 후 파일이 하나 뜸. 해당 파일에다가

  ```python
  alias jp="jupyter notebook"
  ```

  을 적고 저장(`Ctrl` + `S`)하고 끔(`Ctrl` + `w`). 이후에

  ```bash
  $ exec "$SHELL"
  ```

  을 하고나면 이제

  ```bash
  $ jp
  ```

  로 `jupyter noterbook`을 실행할 수 있다.



### 3. 종료

`Ctrl` + `C`





---

---





### (+) Jupyter 사용 방법

- `Enter`치면 Edit(수정)모드
- `ctrl` + `enter` 하면 원래 모드로 돌아옴 - markdown 지원
- `b` 아래, `a`는 위에 블럭 생성
- `dd` 로 삭제
- `markdown` 과 `code`로 2가지 지원(`y`는  code, `m`은 마크다운)
- `code 실행`은 `ctrl+c` (해당 줄 실행) `shift+c` (해당 줄 실행 후 아래로 내려감)

---

- `* `  대기중
- `in [2]`  의 숫자는 실행 번호
- `Kernel` - `restart & clear output` : 뻗거나 작동 안 할 경우 클릭