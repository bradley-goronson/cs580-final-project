def evolution_rule(last_sector_change, alpha, beta, offender_price_change, market_price_change):
  new_sector_change = last_sector_change + alpha*market_price_change + beta*offender_price_change
  return new_sector_change

def cost_function(time_array, alpha, beta, offender_price_change, sector_price, market_price_change):
  estimated_sector_close_array = [sector_price[0]]
  for time in time_array:
    estimated_sector_close_array.append(evolution_rule(estimated_sector_close_array[-1], alpha, beta, offender_price_change[time], market_price_change[time]))
  cost = np.linalg.norm((np.array(sector_price) - np.array(estimated_sector_close_array[1:]))**2)/2
  return cost
