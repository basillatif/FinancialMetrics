import quandl

quandl.ApiConfig.api_key = ###

### To get sector code -> here is the list of codes https://www.zacks.com/zrank/sector-industry-classification.php
data = quandl.get_table('ZACKS/MT', ticker="AXP", qopts={"columns":["ticker", "zacks_x_sector_code", "zacks_x_sector_desc", "zacks_x_ind_code", "zacks_x_ind_desc", "sic_4_code", "sic_4_desc", "zacks_m_ind_code", "zacks_m_ind_desc"]}, paginate = True)
data1 = quandl.get_table('ZACKS/MT', ticker="BA", qopts={"columns":["ticker", "zacks_x_sector_code", "zacks_x_sector_desc", "zacks_x_ind_code", "zacks_x_ind_desc", "sic_4_code", "sic_4_desc", "zacks_m_ind_code", "zacks_m_ind_desc"]}, paginate = True)
#print(data)
#print(data1)

# To get ratio of short term and long term debt
data = quandl.get_table('ZACKS/FR', ticker="AAPL", qopts={"columns":["ticker", "per_end_date", "lterm_debt_cap"]}, paginate=True)
print(data)
