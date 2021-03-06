import glob
import os
import sys

from PIL import Image

tourneys = {'rlcs':'RLCS', 'rlcsx':'RLCS'}
teams = {'rogue':'Rogue', 'rge':'Rogue', 'denial':'Denial Esports', 'den':'Denial Esports', 'dnl':'Denial Esports', 'nrg':'NRG Esports', 'selfless':'Selfless Gaming', 'self':'Selfless Gaming', 'f3':'FlipSid3 Tactics', 'fs3':'FlipSid3 Tactics', 'flipsid3':'FlipSid3 Tactics', 'mock':'Mock-It eSports', 'mock-it':'Mock-It eSports', 'northern':'Northern Gaming', 'ng':'Northern Gaming', 'leftovers':'The Leftovers', 'lo':'The Leftovers', 'as':'Alpha Sydney', 'alpha':'Alpha Sydney', 'jam': 'JAM Gaming'}
scores = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5'}

meta = sys.argv[1].lower();
tourney = tourneys.setdefault(sys.argv[1].lower())
team1 = teams.setdefault(sys.argv[2].lower())
score1 = scores.setdefault(sys.argv[3])
score2 = scores.setdefault(sys.argv[4])
team2 = teams.setdefault(sys.argv[5].lower())

if tourney is not None and team1 is not None and team2 is not None and score1 is not None and score2 is not None:

	tourney_width = int((1024 - 140) / 2)
	tourney_height = 10

	center_width = int((1024 - 430) / 2)

	logo_height = 73
	nameplate_height = 438

	score_width = int((1024 - 62) / 2)
	score_height = 217

	dir = os.path.dirname(os.path.realpath(__file__))
	image = Image.open(dir+"/../imgs/bg.png")
	
	logo = Image.open(dir+"/../imgs/tourney-logos/"+tourney+".png").convert("RGBA")
	logo.thumbnail((140,140))
	image.paste(logo, (tourney_width, tourney_height), mask=logo) 

	team1_nameplate = Image.open(dir+"/../imgs/team-nameplates/"+team1+".png")
	team2_nameplate = Image.open(dir+"/../imgs/team-nameplates/"+team2+".png")
	image.paste(team1_nameplate, (center_width-216, nameplate_height), mask=team1_nameplate) 
	image.paste(team2_nameplate, (center_width+216, nameplate_height), mask=team2_nameplate) 
	
	team1_logo = Image.open(dir+"/../imgs/team-logos/"+team1+".png")
	team2_logo = Image.open(dir+"/../imgs/team-logos/"+team2+".png")
	image.paste(team1_logo, (center_width-216, logo_height), mask=team1_logo) 
	image.paste(team2_logo, (center_width+216, logo_height), mask=team2_logo) 
	
	if meta != 'rlcsx':
		team1_score = Image.open(dir+"/../imgs/score-numbers/"+score1+".png")
		team2_score = Image.open(dir+"/../imgs/score-numbers/"+score2+".png")
		image.paste(team1_score, (score_width-437, score_height), mask=team1_score) 
		image.paste(team2_score, (score_width+437, score_height), mask=team2_score) 

	image.save(dir+"/../output.png","PNG")
else:
	print("Please use the format: python match.py [tourney] [team1] [score1] [score2] [team2]")