def create_pre_cost_matrix(pre_offender_price_change, pre_sector_price_change, pre_market_price_change):
  time_array = list(range(0, pre_sector_price_change.shape[0]))
  pre_cost_matrix = np.zeros((alpha_values.shape[0], alpha_values.shape[0]))
  pre_minimum_cost_and_parameters = (100000, -1, -1)
  for i, beta in enumerate(beta_values):
    for j, alpha in enumerate(alpha_values):
      current_cost = cost_function(time_array, alpha, beta, pre_sector_price_change, pre_market_price_change, pre_offender_price_change)
      pre_cost_matrix[i][j] = current_cost
      if current_cost < pre_minimum_cost_and_parameters[0]:
        pre_minimum_cost_and_parameters = (current_cost, alpha, beta)

  return pre_cost_matrix, pre_minimum_cost_and_parameters

def create_post_cost_matrix(post_offender_price_change, post_sector_price, post_market_price_change):
  time_array = list(range(0, post_sector_price.shape[0]))
  post_cost_matrix = np.zeros((alpha_values.shape[0], alpha_values.shape[0]))
  post_minimum_cost_and_parameters = (100000, -1, -1)
  for i, beta in enumerate(beta_values):
    for j, alpha in enumerate(alpha_values):
      current_cost = cost_function(time_array, alpha, beta, post_sector_price, post_market_price_change, post_offender_price_change)
      post_cost_matrix[i][j] = current_cost
      if current_cost < post_minimum_cost_and_parameters[0]:
        post_minimum_cost_and_parameters = (current_cost, alpha, beta)

  return post_cost_matrix, post_minimum_cost_and_parameters
