from __future__ import division 
from decimal import Decimal
import math

class League:
	def __init__(self):
		self.name = ""
		self.team_list = []

class Hitter :
	
	def __init__ (self): 
		self.games_played=0
		self.pa=0
		self.single=0
		self.id=0
		self.double=0
		self.triple=0
		self.hr=0
		self.rbi=0
		self.r=0
		self.bb=0
		self.so=0
		self.sf=0
		self.bb=0
		self.so=0
		self.ab=0
		self.hit=0
		self.avg=0
		self.slg=0
		self.obp=0
		self.ops=0
		self.bases=0
		self.avg_s=''
		self.slg_s=''
		self.obp_s=''
		self.ops_s=''
		self.name 	= ''
		self.date 	= ''
		self.opp 	= ''
		self.oppID 	= 0
		self.gameID	= 0
		self.memberID = 0
		self.team = None
	
	def stat(self):
		self.hit = self.single+self.double+self.triple+self.hr
		self.bases = self.single+2*self.double+3*self.triple+4*self.hr
		self.ab = self.pa-self.bb-self.sf
		if self.ab!=0 :
			self.avg = self.hit / self.ab 
			self.slg = self.bases / self.ab 
		if self.pa!=0 : 
			self.obp = (self.hit + self.bb) /self.pa 
		self.ops = self.obp + self.slg 

		# map to fix-decimal string
		self.avg_s = format(self.avg, '.3f')
		self.slg_s = format(self.slg, '.3f')
		self.obp_s = format(self.obp, '.3f')
		self.ops_s = format(self.ops, '.3f')

	def add(self, hitter):
		self.pa += hitter.pa
		self.single +=hitter.single
		self.double +=hitter.double
		self.triple +=hitter.triple
		self.hr +=hitter.hr
		self.rbi +=hitter.rbi
		self.r +=hitter.r
		self.bb +=hitter.bb
		self.so +=hitter.so
		self.sf +=hitter.sf
		self.games_played += hitter.games_played



class Pitcher :
	def __init__(self):
		self.games_played=0
		self.win=0
		self.id=0
		self.lose=0
		self.inning=0
		self.pa=0
		self.so=0
		self.bb=0
		self.h=0
		self.hr=0
		self.r=0
		self.outs=0
		self.er=0
		self.go=0
		self.fo=0
		self.era=0
		self.whip=0
		self.bb_inning = 0
		self.era_s=''
		self.whip_s=''
		self.bb_inning_s = ''

	def stat(self):
		self.inning = 0.1*(self.outs%3) + math.floor(self.outs / 3)
		if self.inning !=0 :
			self.era = (self.er / (self.outs /3)) * 7 
			self.whip = (self.h + self.bb) / (self.outs/3)
			self.bb_inning = self.bb / (self.outs / 3)
		else :
			self.era=99
			self.whip=99
			self.bb_inning=99

		# map to fix-decimal string
		self.era_s 		 = format(self.era, '.3f')
		self.whip_s 	 = format(self.whip, '.3f')
		self.bb_inning_s = format(self.bb_inning, '.3f')

	def add(self , pit):
		self.win+=pit.win
		self.lose+=pit.lose
		self.outs +=pit.outs
		self.pa+=pit.pa
		self.so+=pit.so
		self.bb+=pit.bb
		self.h+=pit.h
		self.hr +=pit.hr
		self.r+=pit.r
		self.er+=pit.er
		self.go+=pit.go
		self.fo+=pit.fo
		self.games_played += pit.games_played

class TeamStat:
	def __init__(self):
		self.name 			= ""
		self.teamID 		= 0
		self.current 		= 0
		self.game_played 	= 0
		self.win 			= 0
		self.lose 			= 0
		self.tie  			= 0
		self.percent		= 0.0
		self.GB 			= 0.0
		self.score 			= 0

	def reset(self):
		self.game_played 	= 0
		self.win 		 	= 0
		self.lose 		 	= 0
		self.tie  		 	= 0
		self.percent 	 	= 0.0
		self.GB 		 	= 0.0
		self.score 			= 0

	def stat(self):
		if self.game_played == 0 :
			self.precent = 0
		else :
			self.percent = float(self.win)/(self.win + self.lose)
		self.percent = format(self.percent, '.3f')

class GameStat:
	def __init__(self):
		self.date 		= ""
		self.location 	= ""
		self.opp 		= ""
		self.scores 	= ""
		self.result 	= ""
