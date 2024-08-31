from flask import Flask, render_template, Blueprint

iato = Blueprint('iato', __name__)

@iato.route('/sooo')
def sooo():
    return render_template('Iato/sooo.html')

@iato.route('/osn_sved')
def osn_sved():
    return render_template('Iato/osn_sved.html')

@iato.route('/soy')
def soy():
    return render_template('Iato/soy.html')

@iato.route('/rips')
def rips():
    return render_template('Iato/rips.html')

@iato.route('/doc')
def doc():
    return render_template('Iato/doc.html')

@iato.route('/istor_sprav')
def istor_sprav():
    return render_template('Iato/istor_sprav.html')

@iato.route('/doschool')
def doschool():
    return render_template('Iato/doschool.html')

@iato.route('/local_act')
def local_act():
    return render_template('Iato/local_act.html')

@iato.route('/bez_lich_dann')
def bez_lich_dann():
    return render_template('Iato/bez_lich_dann.html')

@iato.route('/obr')
def obr():
    return render_template('Iato/obr.html')

@iato.route('/rab_prog')
def rab_prog():
    return render_template('Iato/rab_prog.html')

@iato.route('/vneyroch_deyat')
def vneyroch_deyat():
    return render_template('Iato/vneyroch_deyat.html')

@iato.route('/arhiv')
def arhiv():
    return render_template('Iato/arhiv.html')

@iato.route('/sypo')
def sypo():
    return render_template('Iato/sypo.html')

@iato.route('/vpr')
def vpr():
    return render_template('Iato/vpr.html')

@iato.route('/obraz_stand')
def obraz_stand():
    return render_template('Iato/obraz_stand.html')

@iato.route('/fin_xoz_deat')
def fin_xoz_deat():
    return render_template('Iato/fin_xoz_deat.html')

@iato.route('/otch_ob_isp_pxfd')
def otch_ob_isp_pxfd():
    return render_template('Iato/otch_ob_isp_pxfd.html')

@iato.route('/mat_tex_obespech')
def mat_tex_obespech():
    return render_template('Iato/mat_tex_obespech.html')

@iato.route('/school_bib')
def school_bib():
    return render_template('Iato/school_bib.html')

@iato.route('/obor_school_stol')
def obor_school_stol():
    return render_template('Iato/obor_school_stol.html')

@iato.route('/kap_rem')
def kap_rem():
    return render_template('Iato/kap_rem.html')

@iato.route('/plat_obraz_ysl')
def plat_obraz_ysl():
    return render_template('Iato/plat_obraz_ysl.html')

@iato.route('/arhiv_plat_ysl')
def arhiv_plat_ysl():
    return render_template('Iato/arhiv_plat_ysl.html')

@iato.route('/vak_mest_priem')
def vak_mest_priem():
    return render_template('Iato/vak_mest_priem.html')

@iato.route('/stipendii')
def stipendii():
    return render_template('Iato/stipendii.html')

@iato.route('/protiv_kor')
def protiv_kor():
    return render_template('Iato/protiv_kor.html')

@iato.route('/dostyp_sred')
def dostyp_sred():
    return render_template('Iato/dostyp_sred.html')

@iato.route('/zotov')
def zotov():
    return render_template('Iato/zotov.html')

@iato.route('/viday_vipysk')
def viday_vipysk():
    return render_template('Iato/viday_vipysk.html')

@iato.route('/g_i_a')
def g_i_a():
    return render_template('Iato/g_i_a.html')

@iato.route('/org_pit')
def org_pit():
    return render_template('Iato/org_pit.html')

@iato.route('/o_pritm_v_perv_klas')
def o_pritm_v_perv_klas():
    return render_template('Iato/o_pritm_v_perv_klas.html')

@iato.route('/elec_bib')
def elec_bib():
    return render_template('Iato/elec_bib.html')

@iato.route('/povish_kach_obraz')
def povish_kach_obraz():
    return render_template('Iato/povish_kach_obraz.html')

@iato.route('/fynkc_gram')
def fynkc_gram():
    return render_template('Iato/fynkc_gram.html')

@iato.route('/nastav')
def nastav():
    return render_template('Iato/nastav.html')

@iato.route('/kontakti')
def kontakti():
    return render_template('Iato/kontakti.html')

@iato.route('/reg_na_gy')
def reg_na_gy():
    return render_template('Iato/reg_na_gy.html')

@iato.route('/faq')
def faq():
    return render_template('Iato/faq.html')

@iato.route('/distant')
def distant():
    return render_template('Iato/distant.html')

@iato.route('/dosyg_deyat')
def dosyg_deyat():
    return render_template('Iato/dosyg_deyat.html')

@iato.route('/rasp_dis_obuch')
def rasp_dis_obuch():
    return render_template('Iato/rasp_dis_obuch.html')

@iato.route('/doschool_obsh_sved')
def doschool_obsh_sved():
    return render_template('Iato/doschool_obsh_sved.html')

@iato.route('/doschool_dokumenti')
def doschool_dokumenti():
    return render_template('Iato/doschool_dokumenti.html')

@iato.route('/doschool_obrazov')
def doschool_obrazov():
    return render_template('Iato/doschool_obrazov.html')

@iato.route('/doschool_fop')
def doschool_fop():
    return render_template('Iato/doschool_fop.html')

@iato.route('/doschool_komplekt')
def doschool_komplekt():
    return render_template('Iato/doschool_komplekt.html')

@iato.route('/doschool_bezop')
def doschool_bezop():
    return render_template('Iato/doschool_bezop.html')

@iato.route('/doschool_organiz_pit')
def doschool_organiz_pit():
    return render_template('Iato/doschool_organiz_pit.html')

