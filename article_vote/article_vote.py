#!/usr/bin/env python
#coding=utf-8

import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(conn, user, article):
	
	cutoff = time.time() - ONE_WEEK_IN_SECONDS
	if conn.zscore('score:', article) < cutoff:
		return

	article_id = article.partition(':')[-1]
	if conn.sadd('voted:' + article_id, user):
		conn.zincrby('score:', article, VOTE_SCORE)
		conn.hincrby(article, 'votes', 1)

if __name__ == '__main__':
	conn = redis.Redis(host='localhost',port=6379,db=0)
	user = 'user:224397'
	article = 'article:10001'
	article_vote(conn, user, article)
