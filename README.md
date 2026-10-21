# Rosa's Pizza Delivery: Delivery Promise Optimization

## Overview

This project explores how a pizza delivery business can choose promised delivery times to maximize net profit while accounting for the potential costs of late deliveries.

The project includes a Python analysis notebook and an interactive Streamlit application that lets users explore delivery-time recommendations across delivery zones and time blocks.

## Business Problem

A delivery promise involves a trade-off: promising a shorter delivery time may improve the customer experience, but missed promises can lead to refunds and potential customer churn. A longer promise may reduce late-delivery costs but can affect the attractiveness of the service.

The goal is to identify a promising delivery-time commitment under different operating conditions and cost assumptions.

## Approach

- Analyzed delivery-order information from the project dataset.
- Evaluated a discrete set of candidate promised delivery times.
- Compared estimated net profit across candidate promises for a selected zone and time block.
- Built an interactive application to explore recommendations under different financial assumptions.

## Interactive Application

The Streamlit app allows users to:
- Select a delivery zone and time block.
- Adjust the range and step size of candidate delivery promises.
- Change assumptions for order profit margin, churn associated with late orders, and refunds.
- Generate a recommended promise and inspect the estimated profitability.

**Live demo:** [Open the Streamlit app](https://rosa-pizza-delivery-hanna-nguyen.streamlit.app/)

## Tech Stack

- Python
- NumPy
- Streamlit
- Data analysis and discrete optimization

## Repository Structure

- `Pizza Delivery Business Recommendation.ipynb` — exploratory analysis and business recommendations
- `app.py` — interactive Streamlit interface
- `logic.py` — delivery-time evaluation and recommendation logic

## Run Locally

1. Clone this repository.
2. Install the project dependencies using the included project configuration.
3. Start the Streamlit application.

```bash
uv sync
uv run streamlit run app.py
```

If you use a different environment or dependency manager, follow the setup appropriate to your configuration.

## Limitations

The recommendation depends on the dataset and cost assumptions provided to the application. The output is a model-based business recommendation, not a guarantee of actual future profit. Results should be interpreted in light of the assumptions and data limitations.

## AI Assistance and Acknowledgements

This project was completed individually as a class assignment. I designed and implemented the project logic and used Claude (Anthropic) as an AI-assisted development tool to help build the Streamlit interface.

The AI assistance used for this project is documented in the accompanying `AI Appendix.pdf`, which was submitted as part of the assignment.

I reviewed and integrated the resulting code into the project. The appendix provides further details on how AI was used during development.
