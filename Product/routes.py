from flask import request, render_template, Blueprint
from Product.models import prod_models as product
from Product.models import price_models as price
from Product.models import store_models as store

prod_bp = Blueprint('product', __name__, url_prefix='/product')
store_bp = Blueprint('store', __name__, url_prefix='/store')
price_bp = Blueprint('price', __name__, url_prefix='/price')

prod_service = product.Service()
price_service = price.Service()
store_service = store.Service()

# product
@prod_bp.route('/goodInfoAll')
def goodInfoAll():
    goodList = prod_service.getProductInfoAll()
    return render_template('product/goodList.html', goodList=goodList)

@prod_bp.route('/goodInfoOne', methods=['POST'])
def goodInfoOne():
    goodId = request.form['goodId']
    goods = prod_service.getProductInfoOne(goodId)
    return render_template('product/goodOne.html', goods=goods)

@prod_bp.route('/goodInfoByName', methods=['POST'])
def goodInfoByName():
    goodId = request.form['goodId']
    goodList = prod_service.getProductInfoByName(goodId)
    return render_template('product/goodByName.html', goodList=goodList)

# store
@store_bp.route('/storeInfoAll')
def storeInfoAll():
    storeList = store_service.getStoreInfoAll()
    return render_template('store/storeList.html', storeList=storeList)

@store_bp.route('/storeInfoOne', methods=['POST'])
def storeInfoOne():
    entpId = request.form['entpId']
    store = store_service.getStoreInfoOne(entpId)
    return render_template('store/storeOne.html', store=store)

# price
@price_bp.route('/priceByGoodId', methods=['POST'])
def priceInfoByGoodId():
    day = request.form['day']
    goodId = request.form['goodId']
    priceList = price_service.getPriceInfoByGoodId(day, goodId)
    return render_template('price/priceByGoodId.html', priceList=priceList)

@price_bp.route('/priceByEntpId', methods=['POST'])
def priceInfoByEntpId():
    day = request.form['day']
    entpId = request.form['entpId']
    priceList = price_service.getPriceInfoByEntpId(day, entpId)
    return render_template('price/priceByEntpId.html', priceList=priceList)

