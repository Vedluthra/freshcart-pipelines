import pandas as pd
from sklearn.model_selection import train_test_split

# Mage decorators are imported only when the module is running inside Mage.
# This keeps the function importable by pytest and GitHub Actions.
try:
    from mage_ai.data_preparation.decorators import transformer, test
except ImportError:
    def transformer(func):
        return func

    def test(func):
        return func


@transformer
def transform(df, *args, **kwargs):
    """Add a deterministic 80/20 train/test split label to the input DataFrame."""
    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42
    )

    train_df = train_df.copy()
    test_df = test_df.copy()
    train_df["split"] = "train"
    test_df["split"] = "test"

    result = pd.concat([train_df, test_df])
    print("Train rows:", len(train_df), "| Test rows:", len(test_df))
    return result


@test
def test_output(output, *args):
    assert "split" in output.columns, "split column missing"
