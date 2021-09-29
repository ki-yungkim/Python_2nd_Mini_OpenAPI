import requests
from bs4 import BeautifulSoup

# vo

class Store:
    def __init__(self, entpId=None, entpName=None, entpTypeCode=None, entpAreaCode=None, areaDetailCode=None,
                 entpTelno=None, postNo=None, plmkAddrBasic=None, plmkAddrDetail=None, roadAddrBasic=None,
                 roadAddrDetail=None, xMapCoord=None, yMapCoord=None):

        self.entpId = entpId
        self.entpName = entpName
        self.entpTypeCode = entpTypeCode
        self.entpAreaCode = entpAreaCode
        self.areaDetailCode = areaDetailCode
        self.entpTelno = entpTelno
        self.postNo = postNo
        self.plmkAddrBasic = plmkAddrBasic
        self.plmkAddrDetail = plmkAddrDetail
        self.roadAddrBasic = roadAddrBasic
        self.roadAddrDetail = roadAddrDetail
        self.xMapCoord = xMapCoord
        self.yMapCoord = yMapCoord

class Service:
    def __init__(self):
        self.base_url = 'http://openapi.price.go.kr/openApiImpl/ProductPriceInfoService'
        self.api_key = ''

    # 판매점 전체 검색
    def getStoreInfoAll(self):
        cmd = '/getStoreInfoSvc.do?ServiceKey='
        url = self.base_url + cmd + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        stores = []

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.entpInfoVO')
            for item in items:
                entpId = int(item.find('entpId').text)
                entpName = item.find('entpName').text
                entpTypeCode = item.find('entpTypeCode').text
                entpAreaCode = item.find('entpAreaCode').text
                areaDetailCode = item.find('areaDetailCode').text
                if item.find('entpTelno'):
                    entpTelno = item.find('entpTelno').text
                else:
                    entpTelno = None

                if item.find('postNo'):
                    postNo = item.find('postNo').text
                else:
                    postNo = None
                plmkAddrBasic = item.find('plmkAddrBasic').text

                if item.find('plmkAddrDetail'):
                    plmkAddrDetail = item.find('plmkAddrDetail').text
                else:
                    plmkAddrDetail = ''

                if item.find('roadAddrBasic'):
                    roadAddrBasic = item.find('roadAddrBasic').text
                else:
                    roadAddrBasic = None

                if item.find('roadAddrDetail'):
                    roadAddrDetail = item.find('roadAddrDetail').text
                else:
                    roadAddrDetail = None
                if item.find('xMapCoord'):
                    xMapCoord = item.find('xMapCoord').text
                    yMapCoord = item.find('yMapCoord').text
                else:
                    xMapCoord = None
                    yMapCoord = None

                stores.append(Store(entpId=entpId, entpName=entpName, entpTypeCode=entpTypeCode, entpAreaCode=entpAreaCode,
                                    areaDetailCode=areaDetailCode, entpTelno=entpTelno, postNo=postNo,
                                    plmkAddrBasic=plmkAddrBasic, plmkAddrDetail=plmkAddrDetail, roadAddrBasic=roadAddrBasic,
                                    roadAddrDetail=roadAddrDetail, xMapCoord=xMapCoord, yMapCoord=yMapCoord))
            stores.sort(key=lambda Store:Store.entpId)
            return stores

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 판매점 아이디로 검색
    def getStoreInfoOne(self, entpId):
        cmd = '/getStoreInfoSvc.do?entpId='
        url = self.base_url + cmd + entpId + '&ServiceKey=' + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        if code == '00':
            entpId = root.find('entpId').text
            entpName = root.find('entpName').text
            entpTypeCode = root.find('entpTypeCode').text
            entpAreaCode = root.find('entpAreaCode').text
            areaDetailCode = root.find('areaDetailCode').text
            if root.find('entpTelno'):
                entpTelno = root.find('entpTelno').text
            else:
                entpTelno = None

            if root.find('postNo'):
                postNo = root.find('postNo').text
            else:
                postNo = None
            plmkAddrBasic = root.find('plmkAddrBasic').text

            if root.find('plmkAddrDetail'):
                plmkAddrDetail = root.find('plmkAddrDetail').text
            else:
                plmkAddrDetail = None

            if root.find('roadAddrBasic'):
                roadAddrBasic = root.find('roadAddrBasic').text
            else:
                roadAddrBasic = None

            if root.find('roadAddrDetail'):
                roadAddrDetail = root.find('roadAddrDetail').text
            else:
                roadAddrDetail = ''
            if root.find('xMapCoord'):
                xMapCoord = root.find('xMapCoord').text
                yMapCoord = root.find('yMapCoord').text
            else:
                xMapCoord = None
                yMapCoord = None

            return Store(entpId=entpId, entpName=entpName, entpTypeCode=entpTypeCode, entpAreaCode=entpAreaCode,
                         areaDetailCode=areaDetailCode, entpTelno=entpTelno, postNo=postNo,
                         plmkAddrBasic=plmkAddrBasic, plmkAddrDetail=plmkAddrDetail, roadAddrBasic=roadAddrBasic,
                         roadAddrDetail=roadAddrDetail, xMapCoord=xMapCoord, yMapCoord=yMapCoord)

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 판매점 이름으로 검색
    def getStoreByInfoName(self, storeName):
        cmd = '/getStoreInfoSvc.do?ServiceKey='
        url = self.base_url + cmd + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        stores = []

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.entpInfoVO')
            for item in items:
                if storeName in item.find('entpName').text:
                    entpId = int(item.find('entpId').text)
                    entpName = item.find('entpName').text
                    entpTypeCode = item.find('entpTypeCode').text
                    entpAreaCode = item.find('entpAreaCode').text
                    areaDetailCode = item.find('areaDetailCode').text
                    if item.find('entpTelno'):
                        entpTelno = item.find('entpTelno').text
                    else:
                        entpTelno = None

                    if item.find('postNo'):
                        postNo = item.find('postNo').text
                    else:
                        postNo = None
                    plmkAddrBasic = item.find('plmkAddrBasic').text

                    if item.find('plmkAddrDetail'):
                        plmkAddrDetail = item.find('plmkAddrDetail').text
                    else:
                        plmkAddrDetail = ''

                    if item.find('roadAddrBasic'):
                        roadAddrBasic = item.find('roadAddrBasic').text
                    else:
                        roadAddrBasic = None

                    if item.find('roadAddrDetail'):
                        roadAddrDetail = item.find('roadAddrDetail').text
                    else:
                        roadAddrDetail = None
                    if item.find('xMapCoord'):
                        xMapCoord = item.find('xMapCoord').text
                        yMapCoord = item.find('yMapCoord').text
                    else:
                        xMapCoord = None
                        yMapCoord = None

                    stores.append(
                        Store(entpId=entpId, entpName=entpName, entpTypeCode=entpTypeCode,
                              entpAreaCode=entpAreaCode,
                              areaDetailCode=areaDetailCode, entpTelno=entpTelno, postNo=postNo,
                              plmkAddrBasic=plmkAddrBasic, plmkAddrDetail=plmkAddrDetail,
                              roadAddrBasic=roadAddrBasic,
                              roadAddrDetail=roadAddrDetail, xMapCoord=xMapCoord, yMapCoord=yMapCoord))
                    stores.sort(key=lambda Store: Store.entpName)
            return stores

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)



    # 지역별 판매점 수
    def getStoreNumber(self):
        cmd = '/getStoreInfoSvc.do?ServiceKey='
        url = self.base_url + cmd + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.entpInfoVO')
            areas_names = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
                           '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
            areas_cnt = [0] * 17
            num = 0
            for item in items:
                for i in range(0, len(areas_names)):
                    if areas_names[i] in item.find('plmkAddrBasic').text:
                        areas_cnt[i] += 1
                    num += 1
            total_cnt = sum(areas_cnt)
            return areas_names, areas_cnt, total_cnt

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 판매점 주소로 검색
    def getstorebyAddress(self, storeAddress):
        cmd = '/getStoreInfoSvc.do?ServiceKey='
        url = self.base_url + cmd + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        stores = []

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.entpInfoVO')
            for item in items:
                if storeAddress in item.find('plmkAddrBasic').text:
                    entpId = int(item.find('entpId').text)
                    entpName = item.find('entpName').text
                    entpTypeCode = item.find('entpTypeCode').text
                    entpAreaCode = item.find('entpAreaCode').text
                    areaDetailCode = item.find('areaDetailCode').text
                    if item.find('entpTelno'):
                        entpTelno = item.find('entpTelno').text
                    else:
                        entpTelno = None

                    if item.find('postNo'):
                        postNo = item.find('postNo').text
                    else:
                        postNo = None

                    plmkAddrBasic = item.find('plmkAddrBasic').text

                    if item.find('plmkAddrDetail'):
                        plmkAddrDetail = item.find('plmkAddrDetail').text
                    else:
                        plmkAddrDetail = ''

                    if item.find('roadAddrBasic'):
                        roadAddrBasic = item.find('roadAddrBasic').text
                    else:
                        roadAddrBasic = None

                    if item.find('roadAddrDetail'):
                        roadAddrDetail = item.find('roadAddrDetail').text
                    else:
                        roadAddrDetail = None
                    if item.find('xMapCoord'):
                        xMapCoord = item.find('xMapCoord').text
                        yMapCoord = item.find('yMapCoord').text
                    else:
                        xMapCoord = None
                        yMapCoord = None

                    stores.append(
                        Store(entpId=entpId, entpName=entpName, entpTypeCode=entpTypeCode,
                            entpAreaCode=entpAreaCode,
                            areaDetailCode=areaDetailCode, entpTelno=entpTelno, postNo=postNo,
                            plmkAddrBasic=plmkAddrBasic, plmkAddrDetail=plmkAddrDetail,
                            roadAddrBasic=roadAddrBasic,
                            roadAddrDetail=roadAddrDetail, xMapCoord=xMapCoord, yMapCoord=yMapCoord))
                    stores.sort(key=lambda Store: Store.entpId)
            return stores

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)

    # 판매점 아이디, 이름 가져오기
    def getStoreNameList(self):
        cmd = '/getStoreInfoSvc.do?ServiceKey='
        url = self.base_url + cmd + self.api_key
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        stores = []

        if code == '00':
            items = root.find_all('iros.openapi.service.vo.entpInfoVO')
            for item in items:
                entpId = item.find('entpId').text
                entpName = item.find('entpName').text
                stores.append(Store(entpId=entpId, entpName=entpName))

            return stores

        else:
            print('오류 발생 code', code)
            print('오류 발생 메세지', resultMsg)