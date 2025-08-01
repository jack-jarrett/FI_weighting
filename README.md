# Tilted Ladder Weighting Strategy Calculator

This Python script implements a dynamic fixed-income allocation strategy based on the shape of the yield curve. It calculates:

- Asset class weights (Short-term bonds, Floaters, Long bonds, RRBs)
- Maturity bucket allocations across a 10-year ladder

## How It Works

The model uses the **slope of the yield curve** (defined as the 10Y yield minus the 2Y yield) to tilt the portfolio toward:

- Short duration and floaters when the curve is flat or inverted
- Long-term and real-return bonds when the curve is steep

## Formulas Used

### Asset Class Weights
- WS = 0.35 - 0.10 * S
- WF = 0.25 - 0.15 * S
- WL = 0.20 + 0.10 * S
- WR = 0.20 + 0.15 * S

### Maturity Buckets
- Years 1–2 = (2/3) * WS + WF
- Year 3 = (1/3) * WS
- Years 4–6 (RRBs) = (3/7) * WR
- Years 7–10 = (4/7) * WR + WL

### Example Output
Enter the slope value when prompted (e.g., 0.70 if the 10Y yield is 3.47% and 2Y yield is 2.77%).

Asset Class Weights (%):
- Short-term Bonds (WS): 28.0%
- Floaters (WF): 14.5%
- Long-term Bonds (WL): 27.0%
- RRBs (WR): 30.5%

Maturity Bucket Allocations (%):
- Years 1-2 (Short + Floaters): 33.17%
- Year 3 (Short only): 9.33%
- Years 4-6 (RRBs only): 13.07%
- Years 7-10 (RRBs + Long): 44.43%
