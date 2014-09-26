# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Team(models.Model):
	teamID 	= models.AutoField(primary_key=True)
	name 	= models.CharField(max_length=50)
	LEAGUE_NAME =(
		(0,"不存在"),
		(1,"丁丁聯盟"),
		(2,"拉拉聯盟"),
		)
	current = models.IntegerField(max_length=1, choices=LEAGUE_NAME)

	def __unicode__(self):
		return self.name



class Member(models.Model):
	memberID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	studentID = models.CharField(max_length=9)
	number = models.IntegerField(default=0)
	team = models.ForeignKey(Team)
	
	def __unicode__(self):
		return self.name

class Game(models.Model):
	gameID = models.IntegerField(primary_key=True)
	date = models.DateField(blank=True)
	location = models.CharField(max_length=200)
	away = models.ForeignKey(Team, related_name = "awayID")
	home = models.ForeignKey(Team, related_name = "homeID")
	scorebox = models.CharField(max_length=200 ,blank= True)
	away_R = models.IntegerField()
	away_H = models.IntegerField()
	away_E = models.IntegerField()
	home_R = models.IntegerField()
	home_H = models.IntegerField()
	home_E = models.IntegerField()
	record = None

	def __unicode__(self):
		return  self.away.name + ' vs ' + self.home.name + '  ' + str(self.date) 


	def get_scores(self):
		# convert string scorebox: 0,0,0,0,1,0,7;1,0,0,0,1,0
		# to integer array: [[0, 0, 0, 0, 1, 0, 7], [1, 0, 0, 0, 1, 0]]

		 # calculate scorebox if "scores" is empty or "recalculate" is True
		scorebox_str = self.scorebox.split(';')
		score_array = []
		for score_str in scorebox_str :
			score = score_str.split(',')
			score = [int(i) for i in score]
			n = len(score)
			if( n < 7 ):
				for i in range(7-n):
					score.append(0)
			score_array.append(score)

		return score_array

	def get_result(self):
		# return [win_team, lose_team]

		score_array = self.get_scores()

		away_score = sum(score_array[0])
		home_score = sum(score_array[1])

		if( away_score > home_score ):
			return [self.away, self.home]
		elif( home_score > away_score ):
			return [self.home, self.away]
		else: # game tie
			return []


class Pitching(models.Model):
	game = models.ForeignKey(Game)
	member = models.ForeignKey(Member)
	team = models.ForeignKey(Team)
	sequence = models.IntegerField()
	outs = models.IntegerField()
	pa = models.IntegerField()
	h  = models.IntegerField()
	hr = models.IntegerField()
	bb = models.IntegerField()
	so = models.IntegerField()
	r = models.IntegerField()
	er = models.IntegerField()
	go = models.IntegerField()
	fo = models.IntegerField()
	win = models.IntegerField()
	lose = models.IntegerField()
	wl = ''
	IP = ''

	def __unicode__(self):
		return self.member.name + ' ' + str(self.game.date) + ' ' + self.game.home.name + 'vs' + self.game.away.name

	def convert_wl(self):
		if( self.win == 1 ):
			self.wl = "勝"
		elif( self.lose == 1 ):
			self.wl = "敗"

	def calculate_IP(self):
		if( self.outs == 0 ):
			self.IP = '0.0'
		else:
			N = int(self.outs / 3)
			m = self.outs % 3
			self.IP = '%d.%d' %(N, m)

		return self.IP


class Batting(models.Model):
	game = models.ForeignKey(Game)
	member = models.ForeignKey(Member)
	team = models.ForeignKey(Team)
	sequence = models.IntegerField()
	pa = models.IntegerField()
	single = models.IntegerField()
	double = models.IntegerField()
	triple = models.IntegerField()
	hr = models.IntegerField()
	rbi = models.IntegerField()
	run = models.IntegerField()
	bb = models.IntegerField()
	so = models.IntegerField()
	sf = models.IntegerField()
	ab = 0
	def __unicode__(self):
		return self.member.name + ' ' + str(self.game.date) + ' ' + self.game.home.name + 'vs' + self.game.away.name

	def calculate_AB(self):
		self.ab = self.pa - self.bb - self.sf

class Schedule(models.Model):
	date = models.DateField(blank=True)
	time = models.TimeField(blank=True)
	location = models.CharField(max_length=200)
	away = models.ForeignKey(Team, related_name = "away_team")
	home = models.ForeignKey(Team, related_name = "home_team")

	def __unicode__(self):
		return  self.away.name + ' vs ' + self.home.name + '  ' + str(self.date)