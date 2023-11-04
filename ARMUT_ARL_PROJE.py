import random
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option("display.max_columns", None)

df = pd.read_csv("dataset/armut_data.csv")
# df.head()
# df.shape

# ServiceID represents a different service for each CategoryID.
# Create a new variable to represent services by concatenating ServiceID and CategoryID with "_".

df["service_cat_id"] = df["ServiceId"].astype(str) + "_" + df["CategoryId"].astype(str)
df.head()

df[df["UserId"] == 7256]
df["CreateDate"] = pd.to_datetime(df["CreateDate"])
df.info()

df["year"] = df["CreateDate"].dt.year
df["month"] = df["CreateDate"].dt.month
df["year_month"] = df["year"].astype(str) + "_" + df["month"].astype(str)
df["ID"] = df["UserId"].astype(str) + "_" + df["year_month"]
df.head()

#########################
# Creating Association Rules
#########################

pivot_table = df.pivot_table(
    index="ID",
    columns="service_cat_id",
    values="ServiceId",
    aggfunc="count",
    fill_value=0,
)
pivot_table = pivot_table.map(lambda x: True if x > 0 else False)
# pivot_table

frequency_df = apriori(pivot_table, min_support=0.01, use_colnames=True)
frequency_df.head()
frequency_df.sort_values(by="support", ascending=False)

rules = association_rules(frequency_df, metric="support", min_threshold=0.01)

rules["lift"].max()
rules["confidence"].max()
rules["support"].max()

rules[(rules["support"] > 0.015) & (rules["confidence"] > 0.1) & (rules["lift"] > 2.5)]


# Let's use the arl_recommender function to recommend a service to a user who last received service 2_0.
def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

    return recommendation_list[0:rec_count]


random_id = random.choice(df["service_cat_id"])
arl_recommender(rules, "2_0", 3)
arl_recommender(rules, random_id, 5)
