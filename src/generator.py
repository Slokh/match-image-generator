import glob, os

from PIL import Image

dir = os.path.dirname(os.path.realpath(__file__))
image = Image.open(dir+"/../imgs/bg.png")

logo = Image.open(dir+"/../imgs/tourney-logos/RLCS.png").convert("RGBA")
logo.thumbnail((140,140))

team1_nameplate = Image.open(dir+"/../imgs/team-nameplates/G2 Esports.png")
team1_logo = Image.open(dir+"/../imgs/team-logos/G2 Esports.png")
team1_score = Image.open(dir+"/../imgs/score-numbers/3.png")

team2_nameplate = Image.open(dir+"/../imgs/team-nameplates/NRG Esports.png")
team2_logo = Image.open(dir+"/../imgs/team-logos/NRG Esports.png")
team2_score = Image.open(dir+"/../imgs/score-numbers/1.png")

tourney_width = (1024 - 140) / 2
tourney_height = 10

center_width = (1024 - 430) / 2

logo_height = 73
nameplate_height = 438

score_width = (1024 - 62) / 2
score_height = 217

image.paste(logo, (tourney_width, tourney_height), mask=logo) 

image.paste(team1_nameplate, (center_width-216, nameplate_height), mask=team1_nameplate) 
image.paste(team1_logo, (center_width-216, logo_height), mask=team1_logo) 
image.paste(team1_score, (score_width-437, score_height), mask=team1_score) 

image.paste(team2_nameplate, (center_width+216, nameplate_height), mask=team2_nameplate) 
image.paste(team2_logo, (center_width+216, logo_height), mask=team2_logo) 
image.paste(team2_score, (score_width+437, score_height), mask=team2_score) 

image.save(dir+"/../imgs/output.png","PNG")