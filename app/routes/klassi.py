from flask import Flask, render_template, Blueprint

klassi = Blueprint('klassi', __name__)

@klassi.route('/str_klassi')
def str_klassi():
    return render_template('klassi/str_klassi.html')

@klassi.route('/tret_A')
def tret_A():
    return render_template('klassi/tret_A.html')

@klassi.route('/chtr_A')
def chtr_A():
    return render_template('klassi/chtr_A.html')

@klassi.route('/chtr_B')
def chtr_B():
    return render_template('klassi/chtr_B.html')

@klassi.route('/pyat_A')
def pyat_A():
    return render_template('klassi/pyat_A.html')

@klassi.route('/pyat_B')
def pyat_B():
    return render_template('klassi/pyat_B.html')

@klassi.route('/shest_A')
def shest_A():
    return render_template('klassi/shest_A.html')

@klassi.route('/shest_B')
def shest_B():
    return render_template('klassi/shest_B.html')

@klassi.route('/sed_A')
def sed_A():
    return render_template('klassi/sed_A.html')

@klassi.route('/sed_B')
def sed_B():
    return render_template('klassi/sed_B.html')

@klassi.route('/vos_A')
def vos_A():
    return render_template('klassi/vos_A.html')

@klassi.route('/dev_A')
def dev_A():
    return render_template('klassi/dev_A.html')

@klassi.route('/dev_B')
def dev_B():
    return render_template('klassi/dev_B.html')

@klassi.route('/des_A')
def des_A():
    return render_template('klassi/des_A.html')

