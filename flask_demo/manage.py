# -*- coding:utf8 -*-
"""
Created on 2019/9/26 17:18

@author: minc
"""

from flask import Flask, render_template
from flask.json import jsonify

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line

from random import randrange
import datetime,os
from flask import request
import time
from access import getReturnData
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__)


# 使用index01.html自定义模板文件
@app.route("/")
def show_demo01():
    return render_template("chat.html")

@app.route('/post',methods=['POST'])
def post_sentence():
    time.sleep(10)
    sentence = request.json.get("sentence")
    print(sentence)
    ner_result, re_result = getReturnData(sentence)
    ner = ner_result
    option = {
        'title': {
          'text': 'Basic Graph'
        },
        'tooltip': {},
        'animationDurationUpdate': 1500,
        'animationEasingUpdate': 'quinticInOut',
        'series': [
          {
            'type': 'graph',
            'layout': 'force',
            'symbolSize': 50,
            'roam': True,
            'label': {
              'show': True
            },
            'edgeSymbol': ['circle', 'arrow'],
            'edgeSymbolSize': [4, 10],
            'edgeLabel': {
              'fontSize': 20
            },
            'data': [
              { # 实体
                'name': 'Node 1',
              },
              {
                'name': 'Node 2',
              },
              {
                'name': 'Node 3',
              },
              {
                'name': 'Node 4',
              }
            ],
            'links': [ # 关系
              {
                'source': 'Node 1',
                'target': 'Node 2',
                'symbolSize': [5, 20],
                'label': {
                  'show': True,
                  'formatter':"关系1",
                },
                'lineStyle': {
                  'width': 5,
                  'curveness': 0.2
                }
              }
            ],
            'lineStyle': {
              'opacity': 0.9,
              'width': 2,
              'curveness': 0
            }
          }
        ]
      }
    return jsonify({"msg":"提交成功","code":200,"data":{"option":option,'ner':ner}})


if __name__ == "__main__":
    app.run(debug=True)
    # print(BASE_DIR)
    # print(randrange(50, 80))