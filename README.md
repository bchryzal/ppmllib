# PPMLlib

**PPMLlib (Performance Profiles for Machine Learning's library) is a Python library of useful tools for the day-to-day data science and machine learning tasks.**

Author: Chryzal Beaudelaire ZOSSOU <bchryzal@gmail.com>
Date: 2022
Description: Performance Profiles for Machine Learning Python library
License: MIT

<br>

## Installing ppmllib 
To install ppmllib, just execute  

```bash
pip install /path/to/ppmllib-0.1.0-py3-none-any.whl
```

<br>

## Exemple

```python
from ppmllib import ppml
import pandas as pd

# For Regressor Tasks
df = pd.DataFrame()
df['xgb_regressor'] = [1, 3, 3, 3, 2, 2, 3, 3, 1, 2, 3, 5.1, 5, 5, 5, 4]
df['lgb_regressor'] = [1, 2, 3, 2, 3, 3, 2, 2, 1, 2, 3, 3.9, 3, 3, 3, 2]
df['target']  = [0, 4, 3, 1, 3, 3.5, 7, 3, 1, 2, 3, 5, 3, 3, 5, 0]

ppml.PPMLRegressor(
  df,                     # pd.DataFrame
  'target',               # target name
  'your_output_filename'  # output filename
)

# For just plot ppml graph
df_graph = pd.DataFrame()
df_graph['xgboost_classifier']   =  [1, 3, 3, 3, 2, 2, 3, 3, 1, 2, 3, 5, 5, 5, 5, 4]
df_graph['lgbm_classifier']      =  [1, 2, 1, 1, 2, 3, 1, 2, 1, 2, 3, 2, 3, 1, 3, 2]
df_graph['catboost_classifier']  =  [1, 2, 3, 2, 3, 3, 2, 2, 1, 2, 3, 3, 3, 3, 3, 2]

ppml.graph_plot(df_graph, 'your_output_file_name')
```

---

If you use ppmllib as part of your workflow in a scientific publication, please consider citing the ppmllib repository with the following DOI:


```
@article{chryzal_2022_ppmllib,
  author       = {Chryzal Beaudelaire ZOSSOU, V. Ratheil HOUNDJI},
  title        = {PPMLlib: Provide performance profile for machine learning metric in python },
  month        = june,
  year         = 2022,
  url          = {https://github.com/bchryzal/ppmllib/PPforML.pdf}
}
```
- C. Beaudelaire ZOSSOU, V. Ratheil HOUNDJI (2022) PPMLlib: Provide performance profile for machine learning metric in python. Open Source Softw.

---

<br>

## License

- This project is released under a permissive new MIT license ([PPMLlib-LICENSE](https://github.com/bchryzal/ppmllib/LICENSE)) and commercially usable. There is no warranty; not even for merchantability or fitness for a particular purpose.

<br>

## Contact

- bchryzal@gmail.com
