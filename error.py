# -*- coding:utf-8 -*-


class CustomError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
