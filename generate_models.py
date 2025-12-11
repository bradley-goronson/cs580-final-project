def model_function(offender_ticker, treatment_index, offender_price_change, sector_price, market_price_change, left_cutoff=0, right_cutoff=-1):
  pre_cost_matrix, pre_minimum_cost_and_parameters = create_pre_cost_matrix(offender_price_change[left_cutoff:treatment_index], sector_price[left_cutoff:treatment_index], market_price_change[left_cutoff:treatment_index])
  post_cost_matrix, post_minimum_cost_and_parameters = create_post_cost_matrix(offender_price_change[treatment_index:right_cutoff], sector_price[treatment_index:right_cutoff], market_price_change[treatment_index:right_cutoff])

  plot_cost_countours("Cost Contour Over Pre-Treatment Bucket of Models", pre_cost_matrix, pre_minimum_cost_and_parameters)
  plot_3d_cost_surface("Cost Surface Over Pre-Treatment Bucket of Models", pre_cost_matrix, pre_minimum_cost_and_parameters)
  plot_cost_countours("Cost Countour Over Post-Treatment Bucket of Models", post_cost_matrix, post_minimum_cost_and_parameters)
  plot_3d_cost_surface("Cost Surface Over Post-Treatment Bucket of Models", post_cost_matrix, post_minimum_cost_and_parameters)

  pre_alpha = pre_minimum_cost_and_parameters[1]
  pre_beta = pre_minimum_cost_and_parameters[2]
  post_alpha = post_minimum_cost_and_parameters[1]
  post_beta = post_minimum_cost_and_parameters[2]

  optimal_model_estimates, counterfactual_estimates = model_estimates(treatment_index, pre_alpha, pre_beta, post_alpha, post_beta, offender_price_change, sector_price, market_price_change)
  plot_models(offender_ticker, treatment_index, offender_price_change, sector_price, market_price_change, counterfactual_estimates, left_cutoff, right_cutoff)
