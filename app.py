# coding=utf-8
from flask import Flask, request, render_template, url_for
from cloudUtil import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/champions')
def champions():
    heros_list = CloudUtil.queryByField("Heros", "name_cn", "title_cn", "objectId")
    return render_template('champions.html', heros_list=heros_list)


@app.route('/skins/champion/<champion_id>')
def skins_of_champion(champion_id):
    champion = CloudUtil.queryByObjectId("Heros", champion_id)
    skins_list = CloudUtil.queryPointers("Skins", "Heros", champion_id)
    kwargs = dict(champion=champion, skins_list=skins_list)
    return render_template('champion_skins.html', **kwargs)


@app.route('/regions')
def regions():
    region_list = CloudUtil.queryByField("Regions", "name_cn", "objectId")
    kwargs = dict(region_list=region_list, champions_count=champions_count)
    return render_template('regions.html', **kwargs)


@app.route('/champions/region/<region_id>')
def champions_of_region(region_id):
    region = CloudUtil.queryByObjectId("Regions", region_id)
    heros_list = CloudUtil.queryPointers("Heros", "Regions", region_id)
    kwargs = dict(region=region, heros_list=heros_list)
    return render_template('champions.html', **kwargs)


@app.route('/categorys')
def categorys():
    categorys_list = CloudUtil.queryByField("CategoryOfSkins", "name", "objectId")
    return render_template('categorys.html', categorys_list=categorys_list)


if __name__ == '__main__':
    import leancloud

    leancloud.init("9e9v9m1wv7rx2jrppneawb3mm7aphot0j2rxoqqcmval2kzz",
                   "zt57k19dgnks5md0qey4jalvpw39sctrwfjrm6mqm8d44yv7")
    app.run()
