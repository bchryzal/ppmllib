# Chryzal Beaudelaire ZOSSOU 2022
# Performance Profiles for Machine Learning Python library
# Author: Chryzal Beaudelaire ZOSSOU <bchryzal@gmail.com>
#
# License: MIT

from ppmllib.ppml import PPMLRegressor
# from ppmllib import ppml
import pandas as pd

def test_ppml():
  df = pd.DataFrame()
  df['xgb_cls'] = [1, 3, 3, 3, 2, 2, 3, 3, 1, 2, 3, 5.1, 5, 5, 5, 4]
  df['lgb_cls'] = [1, 2, 3, 2, 3, 3, 2, 2, 1, 2, 3, 3.9, 3, 3, 3, 2]
  df['target']  = [0, 4, 3, 1, 3, 3.5, 7, 3, 1, 2, 3, 5, 3, 3, 5, 0]

  PPMLRegressor(df, 'target', 'reg_task')

  # assert 36 == 36