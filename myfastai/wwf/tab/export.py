# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_tab.export.ipynb (unless otherwise specified).

__all__ = ['load_pandas']

# Cell
from fastai.tabular.all import *

# Cell
@patch
def export(self:TabularPandas, fname='export.pkl', pickle_protocol=2):
    "Export the contents of `self` without the items"
    old_to = self
    self = self.new_empty()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        pickle.dump(self, open(Path(fname), 'wb'), protocol=pickle_protocol)
        self = old_to

# Cell
def load_pandas(fname):
    "Load in a `TabularPandas` object from `fname`"
    distrib_barrier()
    res = pickle.load(open(fname, 'rb'))
    return res