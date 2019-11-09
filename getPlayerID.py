# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:37:32 2019

@author: Jack Biscupski
"""

from nba_api.stats.static import players, teams

# simple utility function to wrap nba_api player finder into easy, nice function
def playerID(fullName):
    # find player by full name
    playerDict = players.find_players_by_full_name(fullName)
    
    return playerDict[0]['id']

def teamID(teamName):
    # find team ID by team name
   teamDict = teams.find_teams_by_full_name(teamName)
   if len(teamDict) == 0:
       teamDict = teams.find_teams_by_nickname(teamName)
   return  teamDict[0]['id']
