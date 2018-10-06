# Word Extracter README.	

### 1. 주요 기능

* 한글로 표시된 성경 구절 주소를 참조하여 해당 성경의 영어 버전을 추출해 온다.  
  해당 프로그램은, 성경 공부 교재 영문 번역 시, 수많은 성경 구절의 영어 버전을
  자동으로 추출해 올 수 있는 기능을 제공한다.
* 자료는 'Literal Word' 웹 사이트의 nasb version 영어 성경을 사용한다.
* 주어진 성경 구절 주소를, string parsing 기법으로 parsing 하고 
  nasb.literalword.com 웹사이트에 request를 주고 성경 구절을 받아온다. 
* 'progressbar' 파이썬 library 를 사용하여 현재까지 진행된 상태를 표시한다.



### 2. 구성 환경 

* python 2.7

* library 로 'urllib', 'progressbar' 을 필요로 함.


### 3 . 사용 방법

* 'input.txt' 에 한글 약어로 된 성경 구절 주소를 작성한다.
  주소는 
    '책이름 Chapter:Verses'
  와 같은 형식으로 작성하고 한 줄에 여러 책을 작성하지 않는다. 

  > ```
  > # input.txt 파일 예시
  > 마28:18-20
  > 시119:1-10
  > 요3:16
  > 왕상 3:6-15
  > ```

* input 파일을 'WordExtracter.py' 파일이 있는 디렉토리에 두고 

  ```
  $ python WordExtracter.py
  ```

  와 같이 입력한다.

* 결과는 'WordExtracter.py' 파일이 있는 디렉토리 내에 'output.txt' 라는 이름의 파일에 저장된다.

