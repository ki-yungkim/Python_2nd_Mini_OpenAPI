import requests
from bs4 import BeautifulSoup

# vo

class Standard:
    def __init__(self, code=None, codeName=None):

        self.code = code
        self.codeName = codeName

class Service:
    def __init__(self):
        self.base_url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService/'
        self.api_key = '0T%2F98gSX5j9sCWzfQv5sF20Bt3QHxB0k5iKt4tmI2lofZZemulH7eVuvEyF%2FhonmX4t1s%2Fdk3B%2FpmJ%2FmjoK9pA%3D%3D'

    # 상품 단위 코드
    def getUT(self):
        cmd = 'getStandardInfoSvc.do?classCode='
        url = self.base_url + cmd + 'UT' + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        resultcode = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        std = []
        if resultcode == '00':

            items = root.find_all('iros.openapi.service.vo.stdInfoVO')
            for item in items:
                code = item.find('code').text
                codeName = item.find('codeName').text
                std.append(Standard(code=code, codeName=codeName))
            return std
        else:
            print('오류 발생 code', resultcode)
            print('오류 발생 메세지', resultMsg)

    # 상품 소분류 코드
    def getAL(self):
        cmd = 'getStandardInfoSvc.do?classCode='
        url = self.base_url + cmd + 'AL' + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        resultcode = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        std = []
        if resultcode == '00':

            items = root.find_all('iros.openapi.service.vo.stdInfoVO')
            for item in items:
                code = item.find('code').text
                codeName = item.find('codeName').text
                std.append(Standard(code=code, codeName=codeName))
            return std
        else:
            print('오류 발생 code', resultcode)
            print('오류 발생 메세지', resultMsg)

    # 업체 코드
    def getBU(self):
        cmd = 'getStandardInfoSvc.do?classCode='
        url = self.base_url + cmd + 'BU' + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        resultcode = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        std = []
        if resultcode == '00':

            items = root.find_all('iros.openapi.service.vo.stdInfoVO')
            for item in items:
                code = item.find('code').text
                codeName = item.find('codeName').text
                std.append(Standard(code=code, codeName=codeName))
            return std
        else:
            print('오류 발생 code', resultcode)
            print('오류 발생 메세지', resultMsg)

    # 지역 코드
    def getAR(self):
        cmd = 'getStandardInfoSvc.do?classCode='
        url = self.base_url + cmd + 'AR' + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        resultcode = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        std = []
        if resultcode == '00':

            items = root.find_all('iros.openapi.service.vo.stdInfoVO')
            for item in items:
                code = item.find('code').text
                codeName = item.find('codeName').text
                std.append(Standard(code=code, codeName=codeName))
            return std
        else:
            print('오류 발생 code', resultcode)
            print('오류 발생 메세지', resultMsg)