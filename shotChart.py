# Developer: Jack Biscupski
# Used http://savvastjortjoglou.com/nba-shot-sharts.html as a reference

import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# using James Harden's shot chart/player ID for testing purposes

shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR;'\
                'AMS=2014-15&ContextFilter;=&ContextMeasure;=FGA&DateFrom;=&D;'\
                'ateTo=&GameID;=&GameSegment;=&LastNGames;=0&LeagueID;=00&Loca;'\
                'tion=&MeasureType;=Base&Month;=0&OpponentTeamID;=0&Outcome;=&'\
                'PaceAdjust=N&PerMode;=PerGame&Period;=0&PlayerID;=201935&Plu;'\
                'sMinus=N&Position;=&Rank;=N&RookieYear;=&Season;=2014-15&Seas;'\
                'onSegment=&SeasonType;=Regular+Season&TeamID;=0&VsConferenc;'\
                'e=&VsDivision;=&mode;=Advanced&showDetails;=0&showShots;=1&sh;'\
                'owZones=0'

webdata = requests.get(shot_chart_url)

#headers = webdata.json()

print(webdata.text)

























