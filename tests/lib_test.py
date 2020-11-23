# -*- coding: UTF-8 -*-

# Import from standard library
import os
import potchi
import pandas as pd
# Import from our lib
from potchi.lib import clean_data
import pytest
from potchi.lib import nadege


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(potchi.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

def test_nadege():
    assert nadege(3) == 6
