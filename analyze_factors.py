import pandas as pd
import numpy as np
import sys

# Read the factor data
df = pd.read_excel('data/factor_pricing_data_monthly.xlsx', sheet_name='factors (excess returns)', index_col=0)

print('Date range:', df.index.min(), 'to', df.index.max())
print('Shape:', df.shape)
print('Columns:', list(df.columns))
print('\nFirst 5 rows:')
print(df.head())
print('\nLast 5 rows:')
print(df.tail())

# Calculate full period statistics
full_means = df.mean() * 12  # Annualize
full_vol = df.std() * np.sqrt(12)
full_sharpe = full_means / full_vol

# Filter for 2015-present
df_2015 = df[df.index >= '2015-01-01']
means_2015 = df_2015.mean() * 12  # Annualize
vol_2015 = df_2015.std() * np.sqrt(12)
sharpe_2015 = means_2015 / vol_2015

# Compare
comparison = pd.DataFrame({
    'Full_Mean': full_means,
    'Full_Sharpe': full_sharpe,
    '2015_Mean': means_2015,
    '2015_Sharpe': sharpe_2015,
    'Mean_Change': means_2015 - full_means,
    'Sharpe_Change': sharpe_2015 - full_sharpe
})

print('\n\nFactor Performance Comparison:')
print(comparison.round(4))

print('\n\n2015-Present Statistics:')
print(f"Number of observations: {len(df_2015)}")
print(f"Number of years: {len(df_2015)/12:.1f}")

