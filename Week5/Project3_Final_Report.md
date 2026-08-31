# Project 3 Final Report: Customer Clustering and Segmentation

## Project Objective

The objective of this project was to segment customers into meaningful groups based on their purchasing behaviour using unsupervised machine learning techniques.

The project included:

- K-Means clustering
- DBSCAN clustering
- Feature scaling
- PCA dimensionality reduction
- Cluster evaluation using Silhouette Score
- Visualization
- Business interpretation

## Dataset

The UCI Online Retail dataset was used for this project.

The transaction-level data was cleaned and transformed into customer-level features. After preprocessing, **4,338 customers** were analyzed.

## Customer Features

The following features were used for clustering:

- **Recency:** Days since the customer's most recent purchase.
- **Frequency:** Number of unique invoices.
- **Monetary:** Total amount spent by the customer.
- **Average Order Value:** Average value of customer invoices.
- **Average Quantity:** Average quantity purchased per transaction line.

The features were standardized using StandardScaler before clustering.

## K-Means Clustering

Different values of K were tested using inertia and Silhouette Score.

Final K-Means results:

- **Selected clusters:** 2
- **Silhouette Score:** 0.9759

The high Silhouette Score indicates strong separation between the clusters produced by the model.

## PCA Dimensionality Reduction

PCA was used to reduce the customer features to two principal components for visualization.

The first two principal components explained:

- **72.39% of the total variance**

The PCA visualization was used to observe the separation of the customer clusters.

## DBSCAN Clustering

DBSCAN was applied as a density-based clustering technique.

Final DBSCAN results:

- **Selected eps value:** 0.6
- **Number of clusters:** 2
- **Noise points:** 69

DBSCAN identified observations that did not belong to dense customer groups as noise.

## Comparison of Clustering Methods

| Method | Clusters | Result | Noise Points |
|---|---:|---|---:|
| K-Means | 2 | Silhouette Score: 0.9759 | 0 |
| DBSCAN | 2 | Density-based clustering | 69 |

K-Means produced two clearly separated customer groups. DBSCAN also identified two clusters while detecting 69 unusual observations.

## Business Interpretation

Customer clustering can help businesses:

- Identify high-value and frequent customers for loyalty programs.
- Identify lower-activity customers for re-engagement campaigns.
- Create targeted marketing strategies.
- Investigate unusual purchasing behaviour identified as DBSCAN noise.

The exact business meaning of each cluster can be interpreted using the customer feature profile generated in the notebook.

## Conclusion

This project successfully applied K-Means and DBSCAN clustering to customer purchasing behaviour.

A total of **4,338 customers** were analyzed. K-Means selected **2 customer clusters** with a Silhouette Score of **0.9759**. DBSCAN also identified **2 clusters** and detected **69 noise points**. PCA explained **72.39% of the total variance** using two principal components.

The project demonstrates how unsupervised machine learning can be used to discover customer segments and support data-driven business decisions.
