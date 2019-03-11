# Developer: Jack Biscupski
# Used http://savvastjortjoglou.com/nba-shot-sharts.html as a reference

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from createCourt import create_court
from nba_api.stats.endpoints import shotchartdetail

#sns.set_style('white')
#sns.set_color_codes()

# James Harden
career = shotchartdetail.ShotChartDetail(team_id =1610612745, player_id=201935)
shots = career.get_data_frames()[0]

cmap = plt.cm.viridis
joint_shot_chart = sns.jointplot(shots.LOC_X, shots.LOC_Y, stat_func=None, kind='kde', space=0, color=cmap(.1), cmap=cmap, n_levels=50)
joint_shot_chart.fig.set_size_inches(12,11)
ax = joint_shot_chart.ax_joint
ax.set_xlim(-250, 250)
ax.set_ylim(422.5, -47.5)
 
create_court(ax)
 



















