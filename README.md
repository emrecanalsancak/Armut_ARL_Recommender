# Service Recommendation with Association Rule Learning (ARL)

## Introduction

Armut, Turkey's largest online service platform, connects service providers with customers seeking various services such as cleaning, remodeling, and transportation. In this project, we aim to create a product recommendation system using Association Rule Learning (ARL) based on a dataset containing service users and the services and categories they have received.

## Data Description

The dataset consists of the following variables:

- **UserId**: A unique identifier for customers.
- **ServiceId**: Anonymized services belonging to different categories.
- **CategoryId**: Anonymized categories to which services belong.
- **CreateDate**: The date when a service was purchased.

## Data Preprocessing

1. A new variable, "service_cat_id," is created to represent services by concatenating "ServiceId" and "CategoryId" with "_".
2. The "CreateDate" column is converted to a datetime format for date-related analysis.
3. Additional date-related variables like "year," "month," "year_month," and "ID" are created.

## Association Rule Learning (ARL)

In this project, we use ARL to establish associations between services and recommend them to customers based on their previous interactions.

### Creating Association Rules

1. A pivot table is created to identify whether a customer received a specific service.
2. The Apriori algorithm is applied to the pivot table to determine frequent itemsets.
3. Association rules are generated from frequent itemsets.

### Recommender System

We also implement a recommender system using ARL to suggest services to customers.

- The function `arl_recommender` recommends services to a user based on the association rules.
- Random recommendations are generated for demonstration purposes.

## Usage

You can use the `arl_recommender` function to recommend services for specific users. Replace `"2_0"` with a different `service_cat_id` or pass any random `service_cat_id` to receive recommendations for your desired user.

Example:

```python
arl_recommender(rules, "2_0", 3)  # Recommends 3 services to a user who last received service "2_0".
```
