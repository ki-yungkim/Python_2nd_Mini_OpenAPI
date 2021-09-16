from flask import Flask, request, render_template, redirect, Blueprint
import models as model

bp = Blueprint('product', __name__, url_prefix='/product')

service = model.Service()

@bp.route('/goodInfoAll')
def goodInfoAll():
    goodsList = service.getProductInfoAll()
    return render_template('product/goodList.html', goodsList=goodsList)

@bp.route('/goodInfoOne', methods=['POST'])
def goodInfoOne():
    goodId = request.form['goodId']
    goods = service.getProductInfoOne(goodId)
    return render_template('product/goodOne.html', goods=goods)