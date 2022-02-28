import numpy as np
import pandas as pd


def test_numpy():
    assert np.__version__ > 0


def test_pandas():
    assert pd.__version__ > 0
