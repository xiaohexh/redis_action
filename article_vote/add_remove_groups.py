#!/usr/bin/env python
#coding=utf-8

import redis
import time

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def add_remove_groups(conn, article_id, to_add = [], to_remove = []):
	article = 'article:' + str(article_id)
	for group in to_add:
		conn.sadd('group:' + group, article)
	for group in to_remove:
		conn.srem('group:' + group, article)


if __name__ == '__main__':
	conn = redis.Redis(host='localhost',port=6379,db=0)
	article_id = 10001
	to_add = ['redis', 'programming']
	add_remove_groups(conn, article_id, to_add, [])
