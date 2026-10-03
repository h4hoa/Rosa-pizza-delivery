import numpy as np
import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE

from logic import best_promise, delivery_time_range


@st.cache_data
def cached_time_range():
    shortest, longest = delivery_time_range(ZONES, TIME_BLOCKS, PROMISE)
    return float(shortest), float(longest)


@st.cache_data
def cached_best_promise(zone, time_block, promises, costs):
    best, profit = best_promise(zone, time_block, list(promises), costs)
    return float(best), float(profit)


st.title("Rosa's delivery promise")
st.write("Recommend the promised delivery time that maximises net profit "
         "for a zone and time block, based on the last four weeks of orders.")

shortest_time, longest_time = cached_time_range()

col1, col2 = st.columns(2)
zone = col1.selectbox("Zone", ZONES)
time_block = col2.selectbox("Time block", TIME_BLOCKS)

st.subheader("Promised times to try (minutes)")
col1, col2, col3 = st.columns(3)
start = col1.number_input("Start", value=shortest_time, step=1.0)
end = col2.number_input("End", value=longest_time, step=1.0)
step = col3.number_input("Step", value=5.0, step=1.0)

st.subheader("Costs")
col1, col2, col3 = st.columns(3)
margin = col1.number_input("Profit margin per order ($)",
                           value=float(COSTS['margin']), step=0.5)
churn_orders = col2.number_input("Churn per late order (orders)",
                                 value=float(COSTS['churn_orders']), step=0.1)
refund = col3.number_input("Refund per late order ($)",
                           value=float(COSTS['refund']), step=0.5)

if start >= end:
    st.error("Start must be below end.")
    st.stop()
if step <= 0:
    st.error("Step must be positive.")
    st.stop()
if min(margin, churn_orders, refund) < 0:
    st.error("Costs must not be negative.")
    st.stop()

if st.button("Recommend promise", type="primary"):
    costs = {'refund': refund, 'churn_orders': churn_orders, 'margin': margin}
    # Same range as the notebook:
    # np.arange(shortest_time, longest_time + 2.5, 5), i.e. end included
    promises = tuple(np.arange(start, end + step / 2, step))
    best, profit = cached_best_promise(zone, time_block, promises, costs)
    st.session_state['result'] = {
        'zone': zone, 'time_block': time_block,
        'start': start, 'end': end, 'step': step,
        'costs': costs, 'best': best, 'profit': profit,
    }

result = st.session_state.get('result')
if result:
    st.divider()
    st.subheader(f"Recommendation for {result['zone']} region "
                 f"at {result['time_block']}")
    col1, col2 = st.columns(2)
    col1.metric("Recommended promise", f"{result['best']:.1f} mins")
    col2.metric("Net profit (4 weeks)", f"${result['profit']:,.2f}")
    c = result['costs']
    # "\$" stops Streamlit reading text between two "$" as a LaTeX formula
    st.caption(
        f"Computed for {result['zone']}, {result['time_block']}; "
        f"promises {result['start']:.1f} to {result['end']:.1f} mins "
        f"in steps of {result['step']:g}; margin \\${c['margin']:g}, "
        f"churn {c['churn_orders']:g} orders, refund \\${c['refund']:g}."
    )
    if result['best'] <= result['start'] or result['best'] + result['step'] >= result['end']:
        st.warning("The recommended promise is at the edge of the range "
                   "tried; widen the range in case a better one lies outside.")
    if (result['zone'], result['time_block']) != (zone, time_block):
        st.info("Selection has changed since this result was computed. "
                "Click \"Recommend promise\" to update.")
