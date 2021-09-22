# Python_2nd_Mini_OpenAPI
 
## 210922
## 김기영

 
## 활용 API https://www.data.go.kr/data/3043385/openapi.do

## 팀명 : 3팀 
## 팀원 : 김기영 김현진 박민재 한다예 
## 팀장 : 김기영 

## 주제 : 생필품 가격정보 

## 구현 계획 중인 기능
- 공통 연구 주제 : 주소 활용 방안 탐색

- 1. 코드로 되어있는 것들 값 가져와서 출력 (4번 기능 값 이용)
- 2. 상품 분류별 정보(통계, 가격 변동률 등)
- 12. 업태별 최저가 목록


## 진행 상황 
- getStandardInfoSvc를 standard_models.py 이름으로 정보 가져오기 성공
    - models/standard_models.py
    - templates/standard/ 이하 네개 .py 파일
    - route의 64번째 줄부터 getUT, getAL, getBU, getAR

- 1번 미션 진행 중   
- 생필품 목록 페이지에 코드로 되어있는 것들 기준 데이터 가져와서 알아볼 수 있는 형태의 데이터로 변환 완료
    - templates/product/goodList 수정 적용 (/product/goodInfoAll.html) 
    - 현재 상태 업로드 : 210922_김기영_생필품 목록 코드형 데이터 변환 처리.png


## 210923 계획
- 구현해놓은 페이지들 코드로 되어있는 부분 모드 처리 
- 통계 내는 방법 확인 