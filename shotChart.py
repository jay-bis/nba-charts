# Developer: Jack Biscupski
# Used http://savvastjortjoglou.com/nba-shot-sharts.html as a reference

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

sns.set_style('white')
sns.set_color_codes()


## Anthony Davis
career = shotchartdetail.ShotChartDetail(team_id =1610612740, player_id=203076)
shots = career.get_data_frames()[0]

plt.figure(figsize=(12,11))
plt.scatter(shots.LOC_X, shots.LOC_Y)
plt.show()




















