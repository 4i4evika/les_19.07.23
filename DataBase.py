import sqlite3
import time
import re

from flask import url_for


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_objects(self, table):
        sql = f"SELECT * FROM {table}"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения базы данных')
        return []

    def add_post(self, title, text):
        tm = int(time.time())
        sql = f'INSERT INTO posts VALUES(NULL, ?, ?, ?)'
        try:
            self.__cur.execute(sql, (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False
        return True

    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts1 WHERE id == "{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из базы данных', str(e))
        return None, None