# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-08-13 22:13:52
# @Last Modified by:   Clarence
# @Last Modified time: 2018-08-15 23:50:00
#!/usr/bin/python
#coding=utf-8

"""
框架已经搭建好，大家自己实现
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request

from forms import NewsForm
from redis_news import RedisNews 

app = Flask(__name__)
query = RedisNews()

@app.route('/')
def index():
    """ 新闻首页 """
    news_list = query.get_all_news()
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    news_list = query.get_news_from_cat(name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<pk>/')
def detail(pk):
    """ 新闻详情页 """
    new_obj = query.get_news_from_id(pk)
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    page_data = query.paginage(page, 5)
    return render_template("admin/index.html", page_data=page_data)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    form = NewsForm()
    news_obj = {} # 空的字典保存前台的表单数据
    if form.validate_on_submit():
        """ 这个和更新新闻相反， 我们空的一个form来让用户新增，然后提交获得表单保存到数据库，重定向到首页"""
        news_obj['title'] = form.title.data 
        news_obj['content'] = form.content.data 
        news_obj['news_type'] = form.news_type.data 
        news_obj['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 由于是新增，所以保存新增和更新时间
        news_obj['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        news_obj['is_valid'] = True
        news_obj['img_url'] = form.image.data 
        query.add_news(news_obj)
        flash('新增成功')
        return redirect(url_for('admin'))
    return render_template("admin/add.html", form=form)


@app.route('/admin/update/<pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 更新时间 """
    news_obj = query.get_news_from_id(pk)
    if news_obj is None:
        abort(404)
    """
    form = NewsForm()
    render_template("admin/update.html", form=form)
    提交到update.html中，则新闻标题、新闻内容、新闻类型都默认是空的
    我们需要让用户在原来的数据上修改(get方式请求)，因此先查询到这个数据，然后在将form对象提交到数据库(post方式)
    """
    form = NewsForm(data = news_obj)
    if form.validate_on_submit():
        ''' 用户点击提交按钮，修改数据库对应新闻数据 重定向到首页 '''
        news_obj['title'] = form.title.data 
        news_obj['content'] = form.content.data 
        news_obj['news_type'] = form.news_type.data 
        news_obj['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query.update_news(pk, news_obj)
        flash('修改成功')
        return redirect(url_for('admin'))
    # 用户点击按钮，返回给前台数据展示update.html
    return render_template("admin/update.html", form=form)

@app.route('/admin/delete/<pk>/', methods=['POST'])
def delete(pk):
    ''' 删除新闻 '''
    news_obj = query.get_news_from_id(pk)
    if news_obj:
        query.delete_news(pk, news_obj)
        return 'yes'
    return 'no'

    return 'no'


app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)