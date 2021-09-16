# Python libraries (sys, os, random)

# Standard Data Science libraries
import numpy as np
import pandas as pd

# Extraneous libraries
import pytest

# Local imports
from ..helper_functions import DataFrameFunctions


@pytest.fixture()
def template_df():
    data = {
        'col0': [0, 1, 0, np.NaN, 1, 1],
        'col1': [0, 1, 1, 0, 1, 1],
        'col2': [np.NaN, 0, 1, np.NaN, np.NaN, np.NaN]
    }

    df = pd.DataFrame(data)

    return DataFrameFunctions(df)
