from flask import Flask, render_template, Blueprint

ychit = Blueprint('ychit', __name__)

@ychit.route('/uchitelya_shkoli')
def uchitelya_shkoli():
    return render_template('ychit/uchitelya_shkoli.html')

@ychit.route('/kislova_elena')
def kislova_elena():
    return render_template('ychit/kislova_elena.html')

@ychit.route('/panihina_tatyana')
def panihina_tatyana():
    return render_template('ychit/panihina_tatyana.html')

@ychit.route('/baranova_naezhda')
def baranova_naezhda():
    return render_template('ychit/baranova_naezhda.html')

@ychit.route('/bargan_nadezhda')
def bargan_nadezhda():
    return render_template('ychit/bargan_nadezhda.html')

@ychit.route('/dementeva_valentina')
def dementeva_valentina():
    return render_template('ychit/dementeva_valentina.html')

@ychit.route('/kazarina_maria')
def kazarina_maria():
    return render_template('ychit/kazarina_maria.html')

@ychit.route('/kandalova_olga')
def kandalova_olga():
    return render_template('ychit/kandalova_olga.html')

@ychit.route('/kirsanova_svetlana')
def kirsanova_svetlana():
    return render_template('ychit/kirsanova_svetlana.html')

@ychit.route('/kozireva_irina')
def kozireva_irina():
    return render_template('ychit/kozireva_irina.html')

@ychit.route('/korneeva_olga')
def korneeva_olga():
    return render_template('ychit/korneeva_olga.html')

@ychit.route('/cibin_ivan')
def cibin_ivan():
    return render_template('ychit/cibin_ivan.html')

@ychit.route('/stepanova_mariya')
def stepanova_mariya():
    return render_template('ychit/stepanova_mariya.html')

@ychit.route('/urazhenceva_nadezhda')
def urazhenceva_nadezhda():
    return render_template('ychit/urazhenceva_nadezhda.html')

@ychit.route('/lukyanova_lydmila')
def lukyanova_lydmila():
    return render_template('ychit/lukyanova_lydmila.html')

@ychit.route('/akimova_angelina')
def akimova_angelina():
    return render_template('ychit/akimova_angelina.html')

@ychit.route('/ohrana_truda')
def ohrana_truda():
    return render_template('ychit/ohrana_truda.html')

@ychit.route('/nacional_proekti')
def nacional_proekti():
    return render_template('ychit/nacional_proekti.html')

@ychit.route('/nash_profsoyz')
def nash_profsoyz():
    return render_template('ychit/nash_profsoyz.html')

