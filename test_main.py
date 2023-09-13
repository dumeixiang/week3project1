"""
Test goes here

"""

import polars as pl
from main import development

def test_data():
    # Test with dataset
    data= pl.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
    result = development(data)
    assert result == 47.790116494845364

if __name__ == "__main__":
    test_data()
