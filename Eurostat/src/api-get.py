import eurostat
import sys
import os
from utils.client import EurostatAPIClient

repo = eurostat.get_toc_df()
f = eurostat.subset_toc_df(repo,'Road equipment: load capacity of lorries')


#print(f.axes[0][0])

print(os.getcwd())