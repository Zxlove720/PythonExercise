import pandas as pd
import numpy as np

#
# #1 202358234044 吴振博
# arr = pd.Series([1, 2, 3, 4, 5])
# print(arr)
#
# #2 202358234044 吴振博
# hourly_index = pd.date_range(start='2023-01-01', end='2023-12-31 23:00:00', freq='H')
# print("Hourly Index:")
# print(hourly_index)
#
# weekly_index = pd.date_range(start='2023-01-01', end='2023-12-31', freq='W')
# print("\nWeekly Index:")
# print(weekly_index)
#
# daily_index = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
# print("\nDaily Index:")
# print(daily_index)
#
#
# #3 202358234044 吴振博
index = pd.date_range(start='2023-01-01', periods=12, freq='M')
columns = ['A', 'B', 'C', 'D', 'E']
data = pd.DataFrame(np.random.randn(12, 5), index=index, columns=columns)
# print("\nGenerated 2D Data:")
# print(data)
#
#
# #4 202358234044 吴振博
# random_data = pd.DataFrame(np.random.randn(10, 5))
# print("\n5 Columns of Random Data:")
# print(random_data)
#
#
# #5 202358234044 吴振博
# print("\nDefault Display:")
# print(data)
#
# print("\nFirst 2 Rows:")
# print(data.head(2))
#
# print("\nLast 2 Rows:")
# print(data.tail(2))
#
# print("\nIndex:")
# print(data.index)
# print("Columns:")
# print(data.columns)
# print("Data:")
# print(data.values)
#
# print("\nStatistics:")
# print(data.describe())
#
#
# #6 202358234044 吴振博
# transposed_data = data.T
# print("\nTransposed Data:")
# print(transposed_data)
#
#
# #7 202358234044 吴振博
# sorted_index_asc = data.sort_index()
# print("\nSorted by Index (Ascending):")
# print(sorted_index_asc)
#
# sorted_index_desc = data.sort_index(ascending=False)
# print("\nSorted by Index (Descending):")
# print(sorted_index_desc)
#
# sorted_columns_desc = data.sort_index(axis=1, ascending=False)
# print("\nSorted by Columns (Descending):")
# print(sorted_columns_desc)
#
# sorted_by_A_asc = data.sort_values(by='A')
# print("\nSorted by Column A (Ascending):")
# print(sorted_by_A_asc)
#
#
# #8 202358234044 吴振博
# column_B = data['B']
# print("\nColumn B Data:")
# print(column_B)
#
#
# #9 202358234044 吴振博
# sliced_data = data[:2]
# print("\nSliced Data (First 2 Rows):")
# print(sliced_data)
#
#
# #10 202358234044 吴振博
value_first_row_first_col = data.iloc[0, 0]
print("\nValue at First Row, First Column:")
print(value_first_row_first_col)

subset_data = data.iloc[:3, :4]
print("\nSubset Data (First 3 Rows, First 4 Columns):")
print(subset_data)

top_3_C = data.nlargest(3, 'C')
print("\nTop 3 Rows with Largest C:")
print(top_3_C)