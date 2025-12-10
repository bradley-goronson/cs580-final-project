def process_data(ticker, full_df):
  full_df['price_change_percent'] = full_df['prccd'].pct_change().fillna(0)
  offender_df = full_df[full_df['tic'] == ticker].copy().sort_values('datadate')
  industry_df = full_df[full_df['gind'] == offender_df.iloc[0, 5]].copy().sort_values('datadate')
  industry_df = industry_df[industry_df['tic'] != ticker].copy().sort_values('datadate')
  market_df = full_df[full_df['gind'] != offender_df.iloc[0, 5]].copy().sort_values('datadate')
  axis = np.linspace(0, industry_df['prccd'].size, industry_df['prccd'].size)

  offender_price_change = offender_df[['datadate', 'price_change_percent']].copy().groupby('datadate').mean()
  industry_price_change = industry_df[['datadate', 'price_change_percent']].copy().groupby('datadate').mean()
  market_price_change = market_df[['datadate', 'price_change_percent']].copy().groupby('datadate').mean()

  offender_price_change = np.array(offender_price_change['price_change_percent'])
  industry_price_change = np.array(industry_price_change['price_change_percent'])
  market_price_change = np.array(market_price_change['price_change_percent'])

  #z-score normalize data
  scaler = StandardScaler()
  offender_price_change = scaler.fit_transform(offender_price_change.reshape(-1, 1))
  industry_price_change_price_change = scaler.fit_transform(industry_price_change.reshape(-1, 1))
  market_price_change_price_change = scaler.fit_transform(market_price_change.reshape(-1, 1))

  return offender_price_change, industry_price_change, market_price_change
