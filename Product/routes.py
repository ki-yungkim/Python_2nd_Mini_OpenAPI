from datetime import timedelta
import datetime
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rc
import os
from flask import request, render_template, Blueprint, flash
from Product.models import prod_models as product
from Product.models import price_models as price
from Product.models import store_models as store
from Product.models import standard_models as standard

prod_bp = Blueprint('product', __name__, url_prefix='/product')
store_bp = Blueprint('store', __name__, url_prefix='/store')
price_bp = Blueprint('price', __name__, url_prefix='/price')
standard_bp = Blueprint('standard', __name__, url_prefix='/standard')

prod_service = product.Service()
price_service = price.Service()
store_service = store.Service()
standard_service = standard.Service()

# menu
@prod_bp.route('/')
def product():
    return render_template('product/product.html')

@store_bp.route('/')
def store():
    return render_template('store/store.html')

@price_bp.route('/')
def price():
    return render_template('price/price.html')


# product

# 상품 정보 전체
@prod_bp.route('/goodInfoAll')
def goodInfoAll():
    try:
        goodList = prod_service.getProductInfoAll()
        UTList = standard_service.getUT()
        ALList = standard_service.getAL()
    except:
        flash('상품 데이터가 존재하지 않습니다.')
        goodList = None
    return render_template('product/goodList.html', goodList=goodList, UTList=UTList, ALList=ALList)

# 상품 아이디로 검색
@prod_bp.route('/goodInfoOne', methods=['POST'])
def goodInfoOne():
    goodId = request.form['goodId']
    goodList = prod_service.getProductInfoOne(goodId)
    UTList = standard_service.getUT()
    ALList = standard_service.getAL()
    return render_template('product/goodOne.html', goodList=goodList, UTList=UTList, ALList=ALList)

# 상품 이름으로 검색
@prod_bp.route('/goodInfoByName', methods=['POST'])
def goodInfoByName():
    goodId = request.form['goodId']
    goodList = prod_service.getProductInfoByName(goodId)
    UTList = standard_service.getUT()
    ALList = standard_service.getAL()
    return render_template('product/goodByName.html', goodList=goodList, UTList=UTList, ALList=ALList)

# 전체 목록에서 검색 기능
@prod_bp.route('/goodInfoAll_Search')
def goodInfoAll_Search():
    category = request.args['keyword_category']
    search = request.args['keyword_search']
    UTList = standard_service.getUT()
    ALList = standard_service.getAL()
    try:
        if(category == 'goodAll'):
            goodList = prod_service.getProductInfoAll()
        elif(category == 'goodId'):
            goodList = prod_service.getProductInfoOne(search)
        elif(category == 'goodName'):
            goodList = prod_service.getProductInfoByName(search)

        else:
            flash("일치하는 유형이 없습니다.")
            goodList = None
    except:
        flash("해당 상품 데이터가 존재하지 않습니다.")
        goodList = None

    return render_template('product/goodList.html', goodList=goodList, UTList=UTList, ALList=ALList )
# store

# 판매점 정보 전체
@store_bp.route('/storeInfoAll')
def storeInfoAll():
    storeList = store_service.getStoreInfoAll()
    BUList = standard_service.getBU()
    ARList = standard_service.getAR()
    return render_template('store/storeList.html', storeList=storeList, BUList=BUList, ARList=ARList)

# 판매점 아이디로 검색
@store_bp.route('/storeInfoOne', methods=['POST'])
def storeInfoOne():
    entpId = request.form['entpId']
    store = store_service.getStoreInfoOne(entpId)
    BUList = standard_service.getBU()
    ARList = standard_service.getAR()
    return render_template('store/storeOne.html', store=store, BUList=BUList, ARList=ARList)

# 판매점 이름으로 검색
@store_bp.route('/storeInfoByName', methods=['POST'])
def storeInfoByName():
    entpName = request.form['entpName']
    storeList = store_service.getStoreByInfoName(entpName)
    BUList = standard_service.getBU()
    ARList = standard_service.getAR()
    return render_template('store/storeName.html', storeList=storeList, BUList=BUList, ARList=ARList)

# price

# 상품 아이디로 가격 검색

@price_bp.route('/priceSearch')
def priceSearch():
    return render_template('price/priceSearch.html')

@price_bp.route('/priceByTerm')
def priceByTerm():
    return render_template('price/priceByTerm.html')

@price_bp.route('/priceByGoodId', methods=['POST'])
def priceInfoByGoodId():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    goodId = request.form['goodId']
    priceList = price_service.getPriceInfoByGoodId(day, goodId)
    prodNameList = prod_service.getProductNameList()
    storeNameList = store_service.getStoreNameList()
    return render_template('price/priceByGoodId.html', priceList=priceList, prodNameList=prodNameList, storeNameList=storeNameList)

# 상품 이름으로 가격 검색
@price_bp.route('/priceByGoodName', methods=['POST'])
def priceInfoByGoodName():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    goodName = request.form['goodName']
    priceList = price_service.getPriceInfoByGoodName(day, goodName)
    prodNameList = prod_service.getProductNameList()
    storeNameList = store_service.getStoreNameList()
    return render_template('price/priceByGoodId.html', priceList=priceList, prodNameList=prodNameList, storeNameList=storeNameList)

# 상품 이름으로 할인 판매점, 가격 검색
@price_bp.route('/priceDCByGoodName', methods=['POST'])
def priceInfoDCByGoodName():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    goodName = request.form['goodName']
    priceList = price_service.getDCbyGoodName(day, goodName)
    prodNameList = prod_service.getProductNameList()
    storeNameList = store_service.getStoreNameList()
    return render_template('price/priceByGoodId.html', priceList=priceList, prodNameList=prodNameList, storeNameList=storeNameList)

# 날짜별 상품 가격 최대 최소 평균
@price_bp.route('/priceData', methods=['POST'])
def priceData():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    goodName = request.form['goodName']
    data, entp_max, entp_min = price_service.getPriceData_2(day, goodName)
    storeNameList = store_service.getStoreNameList()

    return render_template('price/priceData.html', goodName=goodName, data=data, entp_max=entp_max, entp_min=entp_min, storeNameList=storeNameList)

# 날짜별 상품 가격 최대 최소 평균 변동률
@price_bp.route('/priceChange', methods=['POST'])
def priceChange():
    day_fromForm_1 = request.form['dayFromForm1']
    day_fromForm_2 = request.form['dayFromForm2']
    day_datetime_1 = datetime.datetime.strptime(day_fromForm_1, '%Y-%m-%d')
    day_datetime_2 = datetime.datetime.strptime(day_fromForm_2, '%Y-%m-%d')
    format = '%Y%m%d'
    day_1 = datetime.datetime.strftime(day_datetime_1, format)
    day_2 = datetime.datetime.strftime(day_datetime_2, format)

    goodName = request.form['goodName']
    data_1 = price_service.getPriceData_1(day_1, goodName)
    data_2 = price_service.getPriceData_1(day_2, goodName)

    avg = round(((data_2[1]-data_1[1])/data_1[1] * 100), 2)
    max = round(((data_2[2]-data_1[2])/data_1[2] * 100), 2)
    min = round(((data_2[3]-data_1[3])/data_1[3] * 100), 2)

    return render_template('price/priceChange.html', goodName=goodName, day_fromForm_1=day_fromForm_1, day_fromForm_2=day_fromForm_2, data_1=data_1, data_2=data_2,  avg=avg, max=max, min=min)

# 날짜 2개 입력 받아서 그 사이 기간 동안 주별 상품 가격 최대 최소 평균
@price_bp.route('/priceChangeWeek', methods=['POST'])
def priceChangeWeek():
    day_fromForm_1 = request.form['dayFromForm1']
    day_fromForm_2 = request.form['dayFromForm2']
    day_datetime_1 = datetime.datetime.strptime(day_fromForm_1, '%Y-%m-%d')
    day_datetime_2 = datetime.datetime.strptime(day_fromForm_2, '%Y-%m-%d')
    day_diff = day_datetime_2 - day_datetime_1
    week_diff = int((str(day_diff / 7))[0])

    format = '%Y%m%d'
    day_start = datetime.datetime.strftime(day_datetime_1, format)
    day_end = datetime.datetime.strftime(day_datetime_2, format)

    day = []
    for i in range(1, week_diff):
        day_datetime_i = day_datetime_1 + timedelta(weeks=i)
        day_i = datetime.datetime.strftime(day_datetime_i, format)
        day.append(day_i)
    goodName = request.form['goodName']

    data_start = price_service.getPriceData_1(day_start, goodName)
    data_end = price_service.getPriceData_1(day_end, goodName)
    data = []
    for i in range(week_diff - 1):
        data_i = price_service.getPriceData_1(day[i], goodName)
        data.append(data_i)

    priceData_avg = []
    priceData_max = []
    priceData_min = []

    priceData_avg.append(data_start[1])
    priceData_avg.append(data_end[1])

    priceData_max.append(data_start[2])
    priceData_max.append(data_end[2])

    priceData_min.append(data_start[3])
    priceData_min.append(data_end[3])

    for i in range(week_diff - 1):
        priceData_avg.append(data[i][1])
        priceData_max.append(data[i][2])
        priceData_min.append(data[i][3])

    return render_template('price/priceDataChange.html', goodName=goodName, week_diff=week_diff, day_fromForm_1=day_fromForm_1,
                           day_fromForm_2=day_fromForm_2, day=day, day_start=day_start, day_end=day_end,
                           priceData_avg=priceData_avg, priceData_max=priceData_max, priceData_min=priceData_min)


# 그래프
@price_bp.route('/priceGraph', methods=['POST'])
def priceGraph():
    day_fromForm_1 = request.form['dayFromForm1']
    day_fromForm_2 = request.form['dayFromForm2']
    day_datetime_1 = datetime.datetime.strptime(day_fromForm_1, '%Y-%m-%d')
    day_datetime_2 = datetime.datetime.strptime(day_fromForm_2, '%Y-%m-%d')
    day_diff = day_datetime_2 - day_datetime_1
    week_diff = int((str(day_diff / 7))[0])

    format = '%Y%m%d'
    day_start = datetime.datetime.strftime(day_datetime_1, format)
    day_end = datetime.datetime.strftime(day_datetime_2, format)

    day = []
    for i in range(1, week_diff):
        day_datetime_i = day_datetime_1 + timedelta(weeks=i)
        day_i = datetime.datetime.strftime(day_datetime_i, format)
        day.append(day_i)
    goodName = request.form['goodName']

    data_start = price_service.getPriceData_1(day_start, goodName)
    data_end = price_service.getPriceData_1(day_end, goodName)
    data = []
    for i in range(week_diff - 1):
        data_i = price_service.getPriceData_1(day[i], goodName)
        data.append(data_i)

    priceData_avg = []
    priceData_max = []
    priceData_min = []

    priceData_avg.append(data_start[1])
    priceData_max.append(data_start[2])
    priceData_min.append(data_start[3])

    for i in range(week_diff - 1):
        priceData_avg.append(data[i][1])
        priceData_max.append(data[i][2])
        priceData_min.append(data[i][3])

    priceData_avg.append(data_end[1])
    priceData_max.append(data_end[2])
    priceData_min.append(data_end[3])

    day.insert(0, day_start)
    day.append(day_end)

    for i in range(len(day)):
        day[i] = day[i][4:]
    font_name = fm.FontProperties(fname='C:\windows/fonts/malgun.ttf').get_name()
    rc('font', family=font_name)

    os.chdir("static/images/")

    plt.plot(day, priceData_avg, 'ro-', label='평균 가격')
    plt.title('평균 가격')
    plt.xlabel('날짜', labelpad=10)
    plt.ylabel('가격 [\\]', labelpad=10)
    plt.legend()
    plt.savefig('avg.png')
    plt.close()

    plt.plot(day, priceData_max, 'bo-', label='최고가')
    plt.title('최고가')
    plt.xlabel('날짜', labelpad=10)
    plt.ylabel('가격 [\\]', labelpad=10)
    plt.legend()
    plt.savefig('max.png')
    plt.close()

    plt.plot(day, priceData_min, 'go-', label='최저가')
    plt.title('최저가')
    plt.xlabel('날짜', labelpad=10)
    plt.ylabel('가격 [\\]', labelpad=10)
    plt.legend()
    plt.savefig('min.png')
    plt.close()

    plt.plot(day, priceData_avg, 'ro-', label='평균가')
    plt.plot(day, priceData_max, 'bo-', label='최고가')
    plt.plot(day, priceData_min, 'go-', label='최저가')
    plt.title('최고, 평균, 최저가')
    plt.xlabel('날짜', labelpad=10)
    plt.ylabel('가격 [\\]', labelpad=10)
    plt.legend()
    plt.savefig('total.png')

    os.chdir("../../")

    return render_template('price/priceDataChange.html', goodName=goodName, week_diff=week_diff, day_fromForm_1=day_fromForm_1,
                           day_fromForm_2=day_fromForm_2, day=day, day_start=day_start, day_end=day_end,
                           priceData_avg=priceData_avg, priceData_max=priceData_max, priceData_min=priceData_min)

# 판매점 아이디로 가격 검색
@price_bp.route('/priceByEntpId', methods=['POST'])
def priceInfoByEntpId():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    entpId = request.form['entpId']
    priceList = price_service.getPriceInfoByEntpId(day, entpId)
    prodNameList = prod_service.getProductNameList()
    storeNameList = store_service.getStoreNameList()
    return render_template('price/priceByEntpId.html', priceList=priceList, prodNameList=prodNameList, storeNameList=storeNameList)

# 판매점 이름로 가격 검색
@price_bp.route('/priceByEntpName', methods=['POST'])
def priceInfoByEntpName():
    day_fromForm = request.form['dayFromForm']
    day_datetime = datetime.datetime.strptime(day_fromForm, '%Y-%m-%d')
    format = '%Y%m%d'
    day = datetime.datetime.strftime(day_datetime, format)

    entpName = request.form['entpName']
    priceList = price_service.getPriceInfoByEntpName(day, entpName)
    prodNameList = prod_service.getProductNameList()
    storeNameList = store_service.getStoreNameList()
    return render_template('price/priceByEntpId.html', priceList=priceList, prodNameList=prodNameList, storeNameList=storeNameList)

# 판매 지역별 업체 수
@store_bp.route('/storeNumber')
def storeNumber():
    areas_names,areas_cnt,total_cnt = store_service.getStoreNumber()

    font_name = fm.FontProperties(fname='C:\windows/fonts/malgun.ttf').get_name()
    rc('font', family=font_name)

    for i in range(len(areas_names)):
        areas_names[i] = areas_names[i][:2]
    labels = areas_names
    data = areas_cnt

    os.chdir("static/images/")
    plt.rcParams['figure.figsize'] = (11, 11)
    plt.rcParams['font.size'] = 11
    plt.pie(data, labels=labels, autopct='%.1f%%', pctdistance=0.7)
    plt.savefig('storeNumber.png')
    plt.close()
    os.chdir("../../")

    return render_template('store/storeNumber.html', a_names = areas_names, a_cnt = areas_cnt,total_cnt=total_cnt)

# 판매점 주소로 검색
@store_bp.route('/storebyAddress', methods=['POST'])
def storebyAddress():
    storeAddress = request.form['storeAddress']
    storeList = store_service.getstorebyAddress(storeAddress)
    listLength = len(storeList)
    BUList = standard_service.getBU()
    ARList = standard_service.getAR()
    return render_template('store/storebyAddress.html', storeList=storeList, listLength=listLength, BUList=BUList, ARList=ARList)


# standard

# 상품 단위 코드
@standard_bp.route('/getUT')
def getUT():
    stdList = standard_service.getUT()
    return render_template('standard/getUT.html', stdList=stdList)

# 상품 소분류 코드
@standard_bp.route('/getAL')
def getAL():
    stdList = standard_service.getAL()
    return render_template('standard/getAL.html', stdList=stdList)

# 업체 코드
@standard_bp.route('/getBU')
def getBU():
    stdList = standard_service.getBU()
    return render_template('standard/getBU.html', stdList=stdList)

# 지역 코드
@standard_bp.route('/getAR')
def getAR():
    stdList = standard_service.getAR()
    return render_template('standard/getAR.html', stdList=stdList)