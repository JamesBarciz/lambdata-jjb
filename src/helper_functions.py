import pandas as pd
import numpy as np


class DataFrameFunctions:

    def __init__(self, df):
        """Constructor"""
        self.df = df

    def null_count(self):
        """
        A function which, given a DataFrame, will return a count of all null values.

        :param df: pd.DataFrame - Pandas DataFrame object
        :return: n_nulls: int - number of null values
        """

        n_nulls = self.df.isna().sum().sum()

        return n_nulls

    def train_test_split(self, frac):
        """
        A function which performs a train-test-split of a Pandas DataFrame into train and test.

        :param self.df: pd.DataFrame - Pandas DataFrame object
        :param frac: float - Proportion of records to attribute to train and test
        :return: train, test: pd.DataFrame objects
        """

        train = self.df.sample(frac=frac, random_state=42)
        test = self.df.drop(train.index)

        return train, test


if __name__ == '__main__':
    data = {
        'col0': [0, 1, 0, np.NaN, 1, 1],
        'col1': [0, 1, 1, 0, 1, 1],
        'col2': [np.NaN, 0, 1, np.NaN, np.NaN, np.NaN]
    }

    df = pd.DataFrame(data)

    data_class = DataFrameFunctions(df)

    print(f'Number of nulls in the DataFrame: {data_class.null_count()}')

    train, test = data_class.train_test_split(frac=0.5)

    print(f'Train has {len(train)} samples')
    print(f'Test has {len(test)} samples')

    print(train)
    print('~~~~~~~~~~~~~~~~')
    print(test)
