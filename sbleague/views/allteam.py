# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Team,Member,Game,Pitching,Batting,Schedule
from data import Hitter, Pitcher, TeamStat, GameStat, League
from operator import attrgetter

def allteam(request,porder='games_played',horder='games_played'):
	teams = Team.objects.filter(current__gt=0)
	allteam_bat = []
	allteam_pit = []
	league_bat = Hitter()
	league_pit = Pitcher()
	for t in teams :
		hitter=Hitter()
		bat_all = Batting.objects.filter(team=t.teamID)
		hitter.name = t.name
		hitter.id = t.teamID
		for bat_detail in bat_all :
			hitter.pa += bat_detail.pa
			hitter.single +=bat_detail.single
			hitter.double +=bat_detail.double
			hitter.triple +=bat_detail.triple
			hitter.hr += bat_detail.hr
			hitter.rbi += bat_detail.rbi
			hitter.r += bat_detail.run
			hitter.bb+= bat_detail.bb
			hitter.so +=bat_detail.so
			hitter.sf +=bat_detail.sf

		pitcher = Pitcher()
		pit_all = Pitching.objects.filter(team=t.teamID)
		pitcher.id = t.teamID
		pitcher.name=t.name
		for pit_detail in pit_all :
			pitcher.win+=pit_detail.win
			pitcher.lose+=pit_detail.lose
			pitcher.outs+=pit_detail.outs
			pitcher.pa+=pit_detail.pa
			pitcher.so+=pit_detail.so
			pitcher.bb+=pit_detail.bb
			pitcher.h+=pit_detail.h
			pitcher.hr+=pit_detail.hr
			pitcher.r+=pit_detail.r
			pitcher.er+=pit_detail.er
			pitcher.go+=pit_detail.go
			pitcher.fo+=pit_detail.fo

		hitter.stat()
		pitcher.stat()
		allteam_bat.append(hitter)
		allteam_pit.append(pitcher)
		league_bat.add(hitter)
		league_pit.add(pitcher)

	league_bat.stat()
	league_pit.stat()

	context={'teams_bat' : allteam_bat , 'teams_pit' : allteam_pit , 'league_bat':league_bat ,'league_pit':league_pit}
	return render(request , 'sbleague/allteam.html',context)