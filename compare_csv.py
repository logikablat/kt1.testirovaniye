import pytest
import pandas as pd
from tabulate import tabulate


def test_compare_csv_files():
    df1 = pd.read_csv('SuperHero.csv')
    df2 = pd.read_csv('SuperHero_updated.csv')

    if not df1.equals(df2):
        diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

        print("\nРазличия между CSV файлами:")
        table = tabulate(diff, headers='keys', tablefmt='grid', showindex=False)
        print(table)


if __name__ == '__main__':
    pytest.main()
