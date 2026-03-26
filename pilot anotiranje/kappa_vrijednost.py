import pandas as pd
import statsmodels.stats.inter_rater as irr

df = pd.read_excel("random_150_rows.xlsx")
ratings_df = df.iloc[:, 6:11]

ratings_raw = ratings_df.to_numpy()

ratings, _ = irr.aggregate_raters(ratings_raw)
kappa = irr.fleiss_kappa(ratings, method="fleiss")

print("Aggregated Ratings Matrix:\n", ratings)
print(f"Fleiss' Kappa: {kappa:.4f}")