---
name: notebook-to-streamlit
description: Use when turning analysis logic from a Jupyter notebook
  into a Streamlit app. Covers extracting notebook code into a pure
  module, mapping notebook variables to widgets, and rerun-safe
  state. Not for building a Streamlit app from scratch, not for
  notebook-only changes.
---


## Step 1 — Extract pure core
Copy the functions the app needs from the notebook into a module
(`logic.py`) with no I/O, no printing, no plotting and no Streamlit
imports. Functions take everything they need as arguments (zone,
time block, promises, costs) rather than reading notebook globals.
Do not rewrite the logic: the module must give the same results as
the notebook. Before going further, call each function with the
notebook's test inputs and confirm the outputs match the notebook's.

## Step 2 — Map the notebook to the interface

| Notebook | Streamlit |
|---|---|
| list of options (`ZONES`, `TIME_BLOCKS`) | `st.selectbox` over that list |
| hardcoded number (a cost, a margin) | `st.number_input`, default = notebook value |
| dictionary of parameters (`COSTS`) | one input per key, rebuilt into a dict with the same keys |
| `range(start, stop, step)` | inputs for start, end and step, defaults = notebook values |
| `print(result)` | `st.metric` / `st.write`, outside the button block |
| a function call in a cell | a button that triggers the call |

Defaults must match the notebook's values, so the app's first result
matches the notebook out of the box.

Validate inputs before computing: the range start must be below the
end, the step must be positive, and costs must not be negative. On
invalid input, show `st.error(...)` and call `st.stop()`.

## Step 3 — State discipline

Streamlit reruns the whole script on every widget interaction.

- Any `if st.button(...)` block should **mutate state only**: compute
  the result and store it in `st.session_state`.
- Rendering happens outside those blocks, reading from
  `st.session_state` unconditionally.
- Store the inputs the result was computed with alongside the
  result, and show them with it, so a changed dropdown never makes
  an old result look like it belongs to the new selection.
- Cache slow, repeated calls to provided data functions with
  `st.cache_data` where their inputs are hashable.

## Step 4 — Deployment readiness

- All dependencies, including any installed from GitHub, are declared
  in `pyproject.toml` and locked in `uv.lock`, so Streamlit Community
  Cloud can install them.
- The app runs from a fresh clone with no notebook state.

## Done when

- [ ] The notebook still runs and gives the same results.
- [ ] `logic.py` reproduces the notebook's test outputs.
- [ ] The app has been tested: click the main button, then change
      another widget, and confirm the result doesn't disappear and
      is still labelled with the inputs it was computed for.
- [ ] With default inputs, the app's recommendation matches the
      notebook's.
