"""Pure logic extracted from "Recommendation for Rosa's pizza delivery
business.ipynb" (Part II). No printing, plotting, file I/O or Streamlit."""

import numpy as np
from starter import delivery_times


def total_cost_per_late_order(costs):
  refund = costs['refund']
  lost_profit = costs['churn_orders'] * costs['margin']
  return round(refund + lost_profit, 2)


def net_profit(zone, time_block, promise, costs):
  # Net profit is the margin earned on all orders
  # minus the cost of the late ones
  times = delivery_times(zone, time_block, promise, seed=42)
  revenue = len(times) * costs['margin']
  late_cost = np.sum(times > promise) * total_cost_per_late_order(costs)
  return revenue - late_cost


def best_promise(zone, time_block, promises, costs):
  profits = {p: net_profit(zone, time_block, p, costs) for p in promises}
  best = max(profits, key=profits.get)
  return round(best, 2), round(profits[best], 2)


def delivery_time_range(zones, time_blocks, promise):
  # Shortest and longest delivery time over all zones and time blocks
  # (notebook Part II b. i.)
  all_times = np.concatenate([delivery_times(z, t, promise, seed=42)
                            for z in zones for t in time_blocks])
  return all_times.min(), all_times.max()
