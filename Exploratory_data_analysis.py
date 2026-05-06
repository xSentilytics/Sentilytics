import pandas as pd

df = pd.read_excel("korpus.xlsx")   


TEXT_COLUMN = "text"      
LABEL_COLUMN = "label"     


print("UKUPNO REDAKA:", len(df))


print("\nLABEL DISTRIBUTION:")
print(df[LABEL_COLUMN].value_counts())


df["word_count"] = df[TEXT_COLUMN].astype(str).apply(lambda x: len(x.split()))


avg_words = df["word_count"].mean()
min_words = df["word_count"].min()
max_words = df["word_count"].max()

print("\nPROSJEČAN BROJ RIJEČI:", round(avg_words,2))
print("NAJMANJA REČENICA:", min_words)
print("NAJVEĆA REČENICA:", max_words)
