import requests
from bs4 import BeautifulSoup
from Product.models import prod_models as prod
from Product.models import store_models as store

prod_service = prod.Service()
store_service = store.Service()
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
        self.api_key = ''

    # 상품 아이디로 가격 검색
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
                if item.find('plusoneYn'):
                    plusoneYn = item.find('plusoneYn').text
                else:
                    plusoneYn = None
                if item.find('goodDcYn'):
                    goodDcYn = item.find('goodDcYn').text
                else:
                    goodDcYn = None
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

    # 상품 이름으로 가격 검색
    def getPriceInfoByGoodName(self, day, goodName):
        goods = prod_service.getProductNameList()
        for good in goods:
            if good.goodName == goodName:
                goodId = good.goodId

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
                if item.find('plusoneYn'):
                    plusoneYn = item.find('plusoneYn').text
                else:
                    plusoneYn = None
                if item.find('goodDcYn'):
                    goodDcYn = item.find('goodDcYn').text
                else:
                    goodDcYn = None
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

    # 상품 이름으로 할인 판매점, 가격 검색
    def getDCbyGoodName(self, day, goodName):
        goods = prod_service.getProductNameList()
        for good in goods:
            if good.goodName == goodName:
                goodId = good.goodId

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
                if item.find('goodDcYn').text == 'Y':
                    print(item.find('goodDcYn').text)
                    goodInspectDay = item.find('goodInspectDay').text
                    entpId = item.find('entpId').text
                    goodId = item.find('goodId').text
                    goodPrice = item.find('goodPrice').text
                    if item.find('plusoneYn'):
                        plusoneYn = item.find('plusoneYn').text
                    else:
                        plusoneYn = None
                    if item.find('goodDcYn'):
                        goodDcYn = item.find('goodDcYn').text
                    else:
                        goodDcYn = None
                    if item.find('goodDcStartDay'):
                        goodDcStartDay = item.find('goodDcStartDay').text
                    else:
                        goodDcStartDay = None

                    if item.find('goodDcEndDay'):
                        goodDcEndDay = item.find('goodDcEndDay').text
                    else:
                        goodDcEndDay = None

                    inputDttm = item.find('inputDttm').text

                    prices.append(
                        Price(goodInspectDay=goodInspectDay, entpId=entpId, goodId=goodId, goodPrice=goodPrice,
                              plusoneYn=plusoneYn, goodDcYn=goodDcYn, goodDcStartDay=goodDcStartDay,
                              goodDcEndDay=goodDcEndDay, inputDttm=inputDttm))
            return prices

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 날짜별 상품 가격 최대 최소 평균
    def getPriceData_1(self, day, goodName):
        goods = prod_service.getProductNameList()
        for good in goods:
            if good.goodName == goodName:
                goodId = good.goodId

        cmd = '/getProductPriceInfoSvc.do?goodInspectDay='
        url = self.base_url + cmd + day + '&goodId=' + goodId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        prices = []
        data = []
        entp_max = []
        entp_min = []
        if code == '00':
            items = root.find_all('iros.openapi.service.vo.goodPriceVO')
            for item in items:
                goodInspectDay = item.find('goodInspectDay').text
                goodPrice = int(item.find('goodPrice').text)
                prices.append(goodPrice)
            data.append(goodInspectDay)
            data.append(round((sum(prices) / len(prices)), 2))
            data.append(max(prices))
            data.append(min(prices))
            for item in items:
                goodPrice = int(item.find('goodPrice').text)
                entpId = item.find('entpId').text
                if goodPrice == max(prices):
                    entp_max.append(entpId)

                elif goodPrice == min(prices):
                    entp_min.append(entpId)

            return data

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 날짜별 상품 가격 최대 최소 평균
    def getPriceData_2(self, day, goodName):
        goods = prod_service.getProductNameList()
        for good in goods:
            if good.goodName == goodName:
                goodId = good.goodId

        cmd = '/getProductPriceInfoSvc.do?goodInspectDay='
        url = self.base_url + cmd + day + '&goodId=' + goodId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        prices = []
        data = []
        entp_max = []
        entp_min = []
        if code == '00':
            items = root.find_all('iros.openapi.service.vo.goodPriceVO')
            for item in items:
                goodInspectDay = item.find('goodInspectDay').text
                goodPrice = int(item.find('goodPrice').text)
                prices.append(goodPrice)
            data.append(goodInspectDay)
            data.append(round((sum(prices) / len(prices)), 2))
            data.append(max(prices))
            data.append(min(prices))
            for item in items:
                goodPrice = int(item.find('goodPrice').text)
                entpId = item.find('entpId').text
                if goodPrice == max(prices):
                    entp_max.append(entpId)

                elif goodPrice == min(prices):
                    entp_min.append(entpId)

            return data, entp_max, entp_min

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 판매점 아이디로 가격 검색
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

    # 판매점 이름로 가격 검색
    def getPriceInfoByEntpName(self, day, entpName):
        stores = store_service.getStoreNameList()
        for store in stores:
            if store.entpName == entpName:
                entpId = store.entpId

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