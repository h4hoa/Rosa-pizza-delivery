This is a course assignment: a Streamlit app that recommends a
promised delivery time for Rosa's delivery business.

## Commands

- `uv add <pkg>` to add dependencies, `uv run ...` to run things.
  Never `pip` or bare `python`.
- App: `uv run streamlit run app.py`
- Dependencies are declared in `pyproject.toml` and locked in
  `uv.lock`; Streamlit Community Cloud installs from these, so commit
  both.

## Architecture

- The course data and simulation come from the instructor's GitHub
  repository (<https://github.com/zhouy185/rosa-starter>), installed in the first cell of the notebook and run every time notebook is opened:
  `!pip install -q git+https://github.com/zhouy185/rosa-starter.git` and imported with
  `from starter import ...`. Do not copy, vendor or edit its
  code. It supplies `ZONES`, `TIME_BLOCKS`, `COSTS`, `PROMISE` and
  `delivery_times(zone, time_block, promise)`, which returns a NumPy
  array of delivery times in minutes for every order in that zone
  and time block over four weeks.
- `Recommendation for Rosa's pizza delivery business.ipynb` holds the original analysis (Parts I and II).
- `logic.py` holds the logic extracted from the notebook:
  `total_cost_per_late_order(costs)`, `net_profit(zone, time_block,
  promise, costs)` and `best_promise(zone, time_block, promises,
  costs)`. Pure functions: no printing, no plotting, no file I/O, no
  streamlit imports. Everything is passed in as arguments.
- `app.py` is a thin wrapper. It collects inputs from widgets, calls
  `logic.py` and displays the result. It contains no profit or
  late-cost calculations of its own.
- A change to `logic.py` must leave the notebook's results
  unchanged.

## Business rules

- An order is late when its delivery time is greater than the
  promise.
- Total cost per late order = refund + churn × profit margin.
- Net profit = number of orders × profit margin − number of late
  orders × cost per late order.
- `delivery_times` depends on the promise, so call it separately for
  each promise tried; never reuse one promise's data for another.

## Constraints

- Standard library plus streamlit, numpy only. Ask before
  adding any other dependency.
- Preserve existing behaviour unless asked to change it.
- Reuse existing code rather than duplicating logic.

