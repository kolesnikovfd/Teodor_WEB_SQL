from flask import Flask
from data.users import User

from data import db_session, __all_models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Grisha'
    user.name = 'Semenov'
    user.age = 25
    user.position = 'oldest helper'
    user.speciality = 'scientist'
    user.address = 'module_4'
    user.email = 'grisha_banditos_228@mars.org'
    db_sess.add(user)
    db_sess.commit()
    '''
    for user in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user)
    #app.run()
    '''


if __name__ == '__main__':
    main()
