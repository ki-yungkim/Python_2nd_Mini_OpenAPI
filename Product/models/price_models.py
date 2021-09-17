import requests
from bs4 import BeautifulSoup

# vo

class Price:
    def __init__(self, goodInspectDay=None, entpId=None, goodId=None, goodPrice=None, plusoneYn=None,
                 goodDcYn=None, goodDcStartDay=None, goodDcEndDay=None, inputDttm=None):

        self.goodInspectDay = goodInspectDay
        self.entpId = entpId
        self.goodId = goodId
        self.goodPrice = goodPrice
        self.plusoneYn = plusoneYn
        self.goodDcYn = goodDcYn
        self.goodDcStartDay = goodDcStartDay
        self.goodDcEndDay = goodDcEndDay
        self.inputDttm = inputDttm

class Service:
    def __init__(self):
        self.base_url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService'
        self.api_key = '0T%2F98gSX5j9sCWzfQv5sF20Bt3QHxB0k5iKt4tmI2lofZZemulH7eVuvEyF%2FhonmX4t1s%2Fdk3B%2FpmJ%2FmjoK9pA%3D%3D'

    def getPriceInfoByGoodId(self, day, goodId):
        cmd = '/getProductPriceInfoSvc.do?goodInspectDay='
        url = self.base_url + cmd + day + '&goodId=' + goodId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        prices = []
        if code == '00':
            items = root.find_all('iros.openapi.service.vo.goodPriceVO')
            for item in items:
                goodInspectDay = item.find('goodInspectDay').text
                entpId = item.find('entpId').text
                goodId = item.find('goodId').text
                goodPrice = item.find('goodPrice').text
                plusoneYn = item.find('plusoneYn').text
                goodDcYn = item.find('goodDcYn').text
                if item.find('goodDcStartDay'):
                    goodDcStartDay = item.find('goodDcStartDay').text
                else:
                    goodDcStartDay = None

                if item.find('goodDcEndDay'):
                    goodDcEndDay = item.find('goodDcEndDay').text
                else:
                    goodDcEndDay = None

                inputDttm = item.find('inputDttm').text

                prices.append(Price(goodInspectDay=goodInspectDay, entpId=entpId, goodId=goodId, goodPrice=goodPrice,
                                    plusoneYn=plusoneYn, goodDcYn=goodDcYn, goodDcStartDay=goodDcStartDay,
                                    goodDcEndDay=goodDcEndDay, inputDttm=inputDttm))
            return prices

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)


    def getPriceInfoByEntpId(self, day, entpId):
        cmd = '/getProductPriceInfoSvc.do?goodInspectDay='
        url = self.base_url + cmd + day + '&entpId=' + entpId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        prices = []

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.goodPriceVO')
            for item in items:
                goodInspectDay = item.find('goodInspectDay').text
                entpId = item.find('entpId').text
                goodId = item.find('goodId').text
                goodPrice = item.find('goodPrice').text
                plusoneYn = item.find('plusoneYn').text
                goodDcYn = item.find('goodDcYn').text

                if item.find('goodDcStartDay'):
                    goodDcStartDay = item.find('goodDcStartDay').text
                else:
                    goodDcStartDay = None

                if item.find('goodDcEndDay'):
                    goodDcEndDay = item.find('goodDcEndDay').text
                else:
                    goodDcEndDay = None
                inputDttm = item.find('inputDttm').text

                prices.append(Price(goodInspectDay=goodInspectDay, entpId=entpId, goodId=goodId, goodPrice=goodPrice,
                                    plusoneYn=plusoneYn, goodDcYn=goodDcYn, goodDcStartDay=goodDcStartDay,
                                    goodDcEndDay=goodDcEndDay, inputDttm=inputDttm))
            return prices

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)