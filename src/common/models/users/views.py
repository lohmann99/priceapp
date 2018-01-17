from flask import Blueprint

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login')
def user_login():
    pass


@user_blueprint.route('/register')
def user_register():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    pass


@user_blueprint.route('/logout')
def user_logout():
    pass


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
