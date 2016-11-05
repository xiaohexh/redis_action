#!/usr/bin/env python
#coding=utf-8

import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
ARTICLE_PER_PAGE = 25

def get_article(conn, page, order='score:'):
	start = (page - 1) * ARTICLE_PER_PAGE
	end = start + ARTICLE_PER_PAGE - 1

	ids = conn.zrevrange(order, start, end)
	articles = []
	for id in ids:
		article_data = conn.hgetall(id)
		article_data['id'] = id
		articles.append(article_data)

	return articles



if __name__ == '__main__':
	conn = redis.Redis(host='localhost',port=6379,db=0)
	articles = get_article(conn, 1)
	for article in articles:
		print article
