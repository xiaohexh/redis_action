#!/usr/bin/env python
#coding=utf-8

import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def post_article(conn, user, title, link):
	article_id = 0
	max_article_id = conn.get('article:');
	print max_article_id
	if max_article_id == None:
		conn.set('article:', 10000)
	article_id = str(conn.incr('article:'))

	voted = 'voted:' + article_id
	conn.sadd(voted, user)
	conn.expire(voted, ONE_WEEK_IN_SECONDS)

	now = time.time()

	article = 'article:' + article_id
	conn.hmset(article, {
		'title': title,
		'link':link,
		'user':user,
		'time':now,
		'votes':1,
	})

	conn.zadd('score:', article, now + VOTE_SCORE)
	conn.zadd('time:', article, now)

	return article_id


if __name__ == '__main__':
	conn = redis.Redis(host='localhost',port=6379,db=0)
	user = 'user:234498'
	title = 'Learning Redis-1'
	link = 'http://www.learning_redis.com/0001'
	article_id = post_article(conn, user, title, link)
	print article_id
