def plot_observations(offender_ticker, treatment_index, offender_price_change, sector_price_change, market_price_change, left_cutoff, right_cutoff):
  axis = np.linspace(0, offender_price_change.shape[0], offender_price_change.shape[0])
  plt.plot(axis[left_cutoff:right_cutoff], offender_price_change[left_cutoff:right_cutoff], color='orange', label=f"{offender_ticker}")
  plt.plot(axis[left_cutoff:right_cutoff], sector_price_change[left_cutoff:right_cutoff], color='green', label="Observed Sector")
  plt.plot(axis[left_cutoff:right_cutoff], market_price_change[left_cutoff:right_cutoff], color='purple', label="Observed Market")
  plt.plot(treatment_index, offender_price_change[treatment_index], 'X', color='red', label="Treatment Date")

  plt.xlabel('Day')
  plt.ylabel('Percent Change in Closing Stock Price')
  plt.title('Observed Price Movement Before and After Treatment')
  plt.legend()

def plot_cost_countours(title, cost_matrix, minimum_cost_and_parameters):
  plt.title(title)
  plt.contourf(alpha_axis, beta_axis, cost_matrix)
  plt.colorbar(label="Model Cost")
  plt.xlabel("α-axis")
  plt.ylabel("β-axis")

  z_point, x_point, y_point = minimum_cost_and_parameters
  plt.plot(x_point, y_point, 'ro', label=f"Minimum Cost Model: α = {round(x_point, 3)} β = {round(y_point, 3)}")

  plt.legend()

def plot_3d_cost_surface(title, cost_matrix, minimum_cost_and_parameters):
  fig = plt.figure(figsize=(7, 7))
  ax = fig.add_subplot(1, 1, 1, projection='3d')

  z_point, x_point, y_point = minimum_cost_and_parameters
  ax.scatter(x_point, y_point, z_point, c='red', marker='o', s=100, label=f"Minimum Cost Model: α = {round(x_point, 3)} β = {round(y_point, 3)}")

  ax.plot_surface(alpha_axis, beta_axis, cost_matrix, cmap="viridis")

  ax.set_xlabel('α-axis')
  ax.set_ylabel('β-axis')
  ax.set_zlabel('Cost-axis')
  ax.set_title(title)

  plt.legend()
  plt.show()
