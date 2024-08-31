from flask import Flask, render_template, Blueprint

shlive = Blueprint('shlive', __name__)

@shlive.route('/sh_gaz')
def sh_gaz():
    return render_template('shlive/sh_gaz.html')

@shlive.route('/sh_teatr')
def sh_teatr():
    return render_template('shlive/sh_teatr.html')

@shlive.route('/olimp')
def olimp():
    return render_template('shlive/olimp.html')

@shlive.route('/profor')
def profor():
    return render_template('shlive/profor.html')

@shlive.route('/inf_dl_rod')
def inf_dl_rod():
    return render_template('shlive/inf_dl_rod.html')

@shlive.route('/o_tebe_sammara')
def o_tebe_sammara():
    return render_template('shlive/o_tebe_sammara.html')

@shlive.route('/uroki_istorii')
def uroki_istorii():
    return render_template('shlive/uroki_istorii.html')

@shlive.route('/mediac')
def mediac():
    return render_template('shlive/mediac.html')

@shlive.route('/profrab')
def profrab():
    return render_template('shlive/profrab.html')

@shlive.route('/let_lag')
def let_lag():
    return render_template('shlive/let_lag.html')

@shlive.route('/bezop')
def bezop():
    return render_template('shlive/bezop.html')

@shlive.route('/dor_bezop')
def dor_bezop():
    return render_template('shlive/dor_bezop.html')

@shlive.route('/shsk')
def shsk():
    return render_template('shlive/shsk.html')

@shlive.route('/vospit_rab')
def vospit_rab():
    return render_template('shlive/vospit_rab.html')

@shlive.route('/ekolog_vospit')
def ekolog_vospit():
    return render_template('shlive/ekolog_vospit.html')

@shlive.route('/proekt_zdor_shc')
def proekt_zdor_shc():
    return render_template('shlive/proekt_zdor_shc.html')

@shlive.route('/volonterstvo')
def volonterstvo():
    return render_template('shlive/volonterstvo.html')

@shlive.route('/meropriyatiya')
def meropriyatiya():
    return render_template('shlive/meropriyatiya.html')

@shlive.route('/proekti')
def proekti():
    return render_template('shlive/proekti.html')

@shlive.route('/bezop_internet')
def bezop_internet():
    return render_template('shlive/bezop_internet.html')

@shlive.route('/proekt')
def proekt():
    return render_template('shlive/proekt.html')

@shlive.route('/urok_franc')
def urok_franc():
    return render_template('shlive/urok_franc.html')

@shlive.route('/front_pisma')
def front_pisma():
    return render_template('shlive/front_pisma.html')

@shlive.route('/kniga_pamyati')
def kniga_pamyati():
    return render_template('shlive/kniga_pamyati.html')

@shlive.route('/metodich_kopilka')
def metodich_kopilka():
    return render_template('shlive/metodich_kopilka.html')

@shlive.route('/sh_muz')
def sh_muz():
    return render_template('shlive/sh_muz.html')

@shlive.route('/posv_75_letiu')
def posv_75_letiu():
    return render_template('shlive/posv_75_letiu.html')

@shlive.route('/prezenac_muz')
def prezenac_muz():
    return render_template('shlive/prezenac_muz.html')

@shlive.route('/nina_lyapina')
def nina_lyapina():
    return render_template('shlive/nina_lyapina.html')

@shlive.route('/uroki_musz')
def uroki_musz():
    return render_template('shlive/uroki_musz.html')

@shlive.route('/alex_alenin')
def alex_alenin():
    return render_template('shlive/alex_alenin.html')

@shlive.route('/zashit_rodini')
def zashit_rodini():
    return render_template('shlive/zashit_rodini.html')

@shlive.route('/zima2021')
def zima2021():
    return render_template('shlive/zima2021.html')

@shlive.route('/gagarinsk_urok')
def gagarinsk_urok():
    return render_template('shlive/gagarinsk_urok.html')

@shlive.route('/prazd_mif')
def prazd_mif():
    return render_template('shlive/prazd_mif.html')

