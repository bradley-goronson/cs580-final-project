# CS 580 Final Project
Project Description: Final project in course on the theory of predictive modeling. Code files for creating dynamic systems models using stock market data before and after a corporate scandal becomes public. Models are designed to explore the effect of the corporate scandal on stock price movements for companies in the same industry as the offending company.

Useful Context: The three titles frequently used for variables in these functions are *offender*, *industry*, and *market*, where the offender is the company that had the corporate scandal, industry is the set of all companies in the same industry as the offender (but not including the offender), and market is the set of all companies not in the same industry as the offender (and therefore not including the industry or offender data). 

The functions used in this project follow the convention of offender > industry > market in the ordering of arguments and return values.  

## File Directory
*process_data.py*    
Functions for processing data before passing to model creation functions. Processing includes calculating z-score normalized percent change in closing stock price for all observerations, and averaging these values grouped by date for the industry and market change arrays. *process_data* function is used when the full data frame includes the offending company. *process_data_with_external_offender_array* is used when it doesn't and the offender array has been prepared separately.

*parameter_space.py*    
Code for setting the alpha and beta ranges used for consturcting the bucket of models and the corresponding meshgrid used to plot cost surfaces.  

*system_definition.py*  
Functions for defining the dynamic system model. The *evolution_rule* function defines the evolution rule, while *cost_function* defines the cost function.  

*cost_matrix.py*  
Functions for generating cost matrices while iterating through the bucket of models. *create_pre_cost_matrix* generates the cost matrix by finding the cost of each parameter combination in the pre-treatment bucket of models and saves the minimal cost and its corresponding parameters. *create_post_cost_matrix* does the same but for the post-treatment bucket of models.  
*model_plots.py*  
Functions used to generate plots after models are created. *plot_observations* plots the observed data and *plot_cost_contours* and *plot_3d_cost_surface* generate a contour or 3D plot of the cost matrix passed to them, along with the minimum cost model represented as a dot on the surface.  

*generate_models.py*  
*model_function* used to generate and plot the models given the offender, industry, and market arrays generated with *process_data.py* functions.

## Usage
### *process_data.py*   

*process_data(ticker, full_df)*  
Arguments:  
- ticker: string  
  - Ticker symbol of the offending company  
- full_df: pandas dataframe  
  - Data frame of all the stock data, including ticker symbols, date, closing stock price, and industry  

Returns:  
- offender_price_change  
- industry_price_change  
- market_price_change

*process_data_with_external_offender_array(full_df, offender_array, offender_industry_code)*   
Arguments:  
- ticker: string  
  - Ticker symbol of the offending company  
- full_df: pandas dataframe  
  - Data frame of all the stock data, including ticker symbols, date, closing stock price, and industry  

Returns:  
- offender_price_change  
- industry_price_change  
- market_price_change

### *parameter_space.py*   
Variables:  
- alpha_values: desired np.linspace array of alpha values for the bucket of models
- beta_values: desired np.linspace array of beta values for the bucket of models
- alpha_axis, beta_axis: meshgrid axes corresponding to alpha_values and beta_values

### *system_definition.py*   
*evolution_rule(last_sector_change, alpha, beta, offender_price_change, market_price_change)*  
Arguments:  
- last_sector_change: float  
  - value of stock price change in the industry in the current state
- alpha: float 
  - alpha parameter 
- beta: float
  - beta parameter
- offender_price_change: float 
  - value of stock price change in the offender in the next state
 - market_price_change: float
  - value of stock price change in the market in the next state

Returns:  
- new_sector_change
  - value of the next state industry price change estimate

*cost_function(time_array, alpha, beta, offender_price_change, sector_price, market_price_change)*   
Arguments:  
- time_array: list  
  - list of integers corresponding to the time periods under consideration (e.g. t = 1, t = 2, etc.)
- alpha: float 
  - alpha parameter 
- beta: float
  - beta parameter
- offender_price_change: ndarray
  - array of stock price changes in the offender
- sector_price: ndarray
  - array of stock price changes in the industry
- market_price_change: ndarray  
  - array of stock price changes in the market

Returns:  
- cost: float
  - norm of error vector of the current model predictions compared to observed data 

### *cost_matrix.py*   
*create_pre_cost_matrix(pre_offender_price_change, pre_sector_price_change, pre_market_price_change)*  
Arguments:  
- pre_offender_price_change: ndarray 
  - array of stock price changes in the offender before the scandal
- pre_sector_price_change: ndarray 
  - array of stock price changes in the industry before the scandal
- pre_offender_price_change: ndarray 
  - array of stock price changes in the market before the scandal

Returns:  
- pre_cost_matrix
  - matrix with the cost values for each parameter combination
- pre_minimum_cost_and_parameters: tuple
  - 3-tuple of the minimum cost found, the alpha of that model, and the beta of that model

*create_post_cost_matrix(post_offender_price_change, post_sector_price, post_market_price_change)*  
Arguments:  
- post_offender_price_change: ndarray 
  - array of stock price changes in the offender after the scandal
- post_sector_price_change: ndarray 
  - array of stock price changes in the industry after the scandal
- post_offender_price_change: ndarray 
  - array of stock price changes in the market after the scandal

Returns:  
- post_cost_matrix
  - matrix with the cost values for each parameter combination
- post_minimum_cost_and_parameters: tuple
  - 3-tuple of the minimum cost found, the alpha of that model, and the beta of that model

### *model_plots.py*   
*plot_observations(offender_ticker, treatment_index, offender_price_change, sector_price_change, market_price_change, counterfactual_estimates, left_cutoff, right_cutoff)*  
Arguments:  
- offender_ticker: string  
  - Ticker symbol of offending company
- treatment_index: int 
  - index where the scandal occured in the data
- offender_price_change: ndarray 
  - array of stock price changes in the offender
- sector_price_change: ndarray 
  - array of stock price changes in the industry
- market_price_change: ndarray
  - array of stock price changes in the market
- left_cutoff: int
  - first index to plot
- right_cutoff: int
  - last index to plot

