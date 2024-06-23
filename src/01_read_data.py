import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import datetime

from movingpandas import Trajectory
from functions.handler_gpx import gpx_to_traj
from functions.handler_categories import create_categories
from functions.handler_pick_urls import create_url

GPX_NAME = 'data/Schoonwandelen_714_items.gpx'
XLS_NAME = 'scratch/final_pick_data.xlsx'

# import movement data
traj = gpx_to_traj(GPX_NAME)

# import picks
picks = pd.read_excel(XLS_NAME, header=0, index_col=0)
picks = gpd.GeoDataFrame(picks,
                         geometry=gpd.points_from_xy(picks.lon, picks.lat),
                         crs="EPSG:4326")

# subtract 2 hours from the timestamp
picks['date_taken'] = picks['date_taken'] - datetime.timedelta(hours=2)


# create urls
picks = create_url(picks)

# save data in scratch as geojson
picks.to_file("scratch/picks.geojson", driver='GeoJSON')

gdf = traj.df  # Convert to GeoDataFrame
gdf.to_file("scratch/traj.geojson", driver='GeoJSON')