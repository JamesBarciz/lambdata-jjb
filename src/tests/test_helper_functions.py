import pandas as pd


def test_class_contains_df(template_df):
    assert hasattr(template_df, 'df')
    assert isinstance(template_df.df, pd.DataFrame)


def test_null_count(template_df):
    assert template_df.null_count() == 5


def test_train_test_split(template_df):
    train, test = template_df.train_test_split(frac=0.5)

    assert len(train) == 3
    assert len(test) == 3

    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)
