import  pandas as pd

# data of PCT is in census_starter.py 
# its column based - identifier column cfips & yearly pcts are there .

# data of microbusinessdensity is in train.csv - identifier cfips +month


# Load key_attributes.csv file
key_attributes_df = pd.read_csv('census_starter.csv')

# Unpivot the percentage of broadband access columns
pct_bb_cols = [col for col in key_attributes_df.columns if col.startswith('pct_bb')]
key_attributes_df = key_attributes_df.melt(id_vars=['cfips'], value_vars=pct_bb_cols, var_name='year', value_name='pct_bb')

# Unpivot the percentage of college-educated columns
pct_college_cols = [col for col in key_attributes_df.columns if col.startswith('pct_college')]
key_attributes_df = key_attributes_df.melt(id_vars=['cfips'], value_vars=pct_college_cols, var_name='education', value_name='pct_college')

# Unpivot the percentage of foreign-born columns
pct_foreign_cols = [col for col in key_attributes_df.columns if col.startswith('pct_foreign_born')]
key_attributes_df = key_attributes_df.melt(id_vars=['cfips'], value_vars=pct_foreign_cols, var_name='foreign_born', value_name='pct_foreign')

# Unpivot the percentage of IT workers columns
pct_it_cols = [col for col in key_attributes_df.columns if col.startswith('pct_it_workers')]
key_attributes_df = key_attributes_df.melt(id_vars=['cfips'], value_vars=pct_it_cols, var_name='job_type', value_name='pct_it_workers')

# Unpivot the median household income columns
median_hh_cols = [col for col in key_attributes_df.columns if col.startswith('median_hh_inc')]
key_attributes_df = key_attributes_df.melt(id_vars=['cfips'], value_vars=median_hh_cols, var_name='income_type', value_name='median_hh_inc')

key_attributes_df.describe()
# Flatten the column names
# pivoted_df.columns = [f'{col[0]}_{col[1]}' for col in pivoted_df.columns]

# pivoted_df.describe()
# # Load test.csv file
# test_df = pd.read_csv('train.csv')

# # Merge the data frames
# merged_df = pd.merge(test_df, pivoted_df, on='cfips')

