from flask import (
    request,
    render_template,
    Blueprint,
    make_response,
)

from .objects import cookie_user_dict

clearMine_blueprint = Blueprint('main', __name__)


@clearMine_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """回馈login页面"""
    return render_template('login.html')


@clearMine_blueprint.route('/minesweeper', methods=['GET', 'POST'])
def mine():
    """判断权限, 对有权限者回馈扫雷游戏页面"""
    res = '无权限'
    try:
        if request.args['uname'] in cookie_user_dict:
            res = make_response(render_template('minesweeper.html'))
        else:
            res += ', 请重新登录'
    except Exception as e:
        print(e)
    return res


@clearMine_blueprint.route('/ranks', methods=['GET', 'POST'])
def total_rank():
    """判断权限, 对有权限者回馈扫雷战绩总榜页面"""
    res = '无权限'
    try:
        if request.args['uname'] in cookie_user_dict:
            res = make_response(render_template('ranks.html'))
        else:
            res += ', 请重新登录'
    except Exception as e:
        print(e)
    return res
