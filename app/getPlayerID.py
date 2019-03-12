# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:37:32 2019

@author: Jack Biscupski
"""

from nba_api.stats.static import players

def playerID(fullName):
    # find player by full name
    playerDict = players.find_players_by_full_name(fullName)
    
    return playerDict[0]['id']
    