# -*- coding:utf-8 -*-

import random
import time
import requests, bs4
import urllib.request
import sys
import os
import codecs

"""
    使い方：　python TalkGet.py [URL] [File]
    URLにあるトークメーカーのストーリーを取得してTextディレクトリにxhtmlページ(file)を作成します。
    自動的に画像も取得します。
    できたxhtmlファイルはSigilにつっこみ、表紙と目次等を追加すればEpub化できます。
    今のところは吹き出し表示と背景色はナシ。
"""
#定数的ないろいろ
#改行コード
CR = chr(13)    #Mac

# 不要タグ除去
def divCng():
    #download(url,'work.html')
    file = codecs.open('Text/worktout.xhtml' ,'w','utf-8')

    lineCount = 0
    for Line in codecs.open("worktext.dat", "r",'utf-8'):
        lineCount += 1
        Line = Line.replace('<div>','')
        ##Line = Line.replace('</div>','')
        file.write(Line)
    file.close()



if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    divCng()


##print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する
