from Utils.mainUtils import *
# Import mainUtils

# Import all functions from other files
from Functions.Events.on_guild_join_leave import on_guild_join as on_guild_join_func, on_guild_remove as on_guild_remove_func

# This file will be imported in main.py using a single line. This helps to keep main.py as small as possible and move all functional code to other files.