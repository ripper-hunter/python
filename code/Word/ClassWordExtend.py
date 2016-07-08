#encodig=utf-8
# _*_ coding:utf-8 _*_
# Writer : lgy
# dateTime : 2016-07-08

import sys
sys.path.append("/home/spark1/python/")
sys.path.append("/home/spark/anqu/python/code")
sys.path.append("/home/spark/anqu/python/code/Tools")
sys.path.append("/home/spark/anqu/python/code/data_deal")
sys.path.append("/home/spark/anqu/python/code/Cluster")
sys.path.append("/home/spark/anqu/python/code/Word")
reload(sys)
sys.setdefaultencoding('utf8') 

from mysql_op import mysql_op
from data_deal import data_deal
from chinese import chinese

#类别词的拓展
class ClassWordExtend():
	def __init__(self):
		pass

	#根据应用的ID获取品类下的关联词
	def getGenreIDByAppId(self,AppIds):
		mysql = mysql_op()
		genreIds = []
		for appid in AppIds:
			sql = 'select genreID from appInfo where appID=%d'%appid
			data = mysql.getWordPriority(sql)[0][0]
			if data == None or len(data) == 0:
				continue
			data = data.split(",")
			genreIds += data
		return list(set(genreIds))

	#获取类别的下的关键词
	def getKeyWordofClassWord(self,genreIds):
		sql = 'select word,genre from ansearchApp'
		mysql = mysql_op()
		words = mysql.getWordPriority(sql)
		print words[0]
		word_re = []
		chi = chinese()
		for word in words:
			for genreId in genreIds:
				if genreId in word[1].split(','):
					if chi.is_chinese(word[0]):
						word_re.append(word[0])
					break
		return list(set(word_re))

def main():
	cwd = ClassWordExtend()
	genreIds = cwd.getGenreIDByAppId([284087761,284124560,284146702])
	word_re = cwd.getKeyWordofClassWord(genreIds)
	# for word in word_re:
		# print word
	print len(word_re)
if __name__ == '__main__':
	main()