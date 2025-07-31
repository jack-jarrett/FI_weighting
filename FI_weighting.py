# Tilted Yield Ladder Strategy Weighting Calculator

def calculate_weights(slope):
    # Step 1: Asset Class Weights based on yield curve slope (S)
    WS = 0.35 - 0.10 * slope  # Short-term Bonds
    WF = 0.25 - 0.15 * slope  # Floaters
    WL = 0.20 + 0.10 * slope  # Long-term Bonds
    WR = 0.20 + 0.15 * slope  # RRBs

    # Step 2: Maturity Bucket Allocation
    buckets = {
        "Years 1-2 (Short + Floaters)": (2/3)*WS + WF,
        "Year 3 (Short only)": (1/3)*WS,
        "Years 4-6 (RRBs only)": (3/7)*WR,
        "Years 7-10 (RRBs + Long)": (4/7)*WR + WL
    }

    # Step 3: Output
    asset_class_weights = {
        "Short-term Bonds (WS)": round(WS * 100, 2),
        "Floaters (WF)": round(WF * 100, 2),
        "Long-term Bonds (WL)": round(WL * 100, 2),
        "RRBs (WR)": round(WR * 100, 2)
    }

    maturity_buckets = {
        key: round(value * 100, 2) for key, value in buckets.items()
    }

    return asset_class_weights, maturity_buckets

# Example usage
if __name__ == "__main__":
    slope_input = float(input("Enter the yield curve slope (10Y - 2Y yield): "))
    asset_weights, bucket_allocations = calculate_weights(slope_input)

    print("\nAsset Class Weights (%):")
    for k, v in asset_weights.items():
        print(f"{k}: {v}%")

    print("\nMaturity Bucket Allocations (%):")
    for k, v in bucket_allocations.items():
        print(f"{k}: {v}%")

