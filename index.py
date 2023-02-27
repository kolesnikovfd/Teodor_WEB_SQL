from flask import Flask
from data.users import User

from data import db_session, __all_models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.db')
    '''user = User()
    user.name = "Пользователь 3"
    user.about = "биография пользователя 3"
    user.email = "email@email3.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()'''
    #app.run()


if __name__ == '__main__':
    main()
