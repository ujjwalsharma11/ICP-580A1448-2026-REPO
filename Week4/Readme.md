# Week 4 – Project 3: Customer Clustering

## Project Overview

This week focuses on Customer Clustering and Segmentation using unsupervised machine learning techniques.

The objective is to group customers based on their purchasing behaviour and identify meaningful customer segments.

## Dataset

The UCI Online Retail dataset was used for this project.

The transaction data was cleaned and transformed into customer-level features.

## Work Completed

The following tasks were completed:

- Loaded and cleaned the dataset
- Created customer-level features
- Applied feature scaling using StandardScaler
- Applied K-Means clustering
- Evaluated different numbers of clusters
- Used Silhouette Score for cluster evaluation
- Applied PCA for dimensionality reduction
- Visualized customer clusters
- Applied DBSCAN clustering
- Identified DBSCAN noise points
- Compared K-Means and DBSCAN results

## Features Used

The customer features used for clustering were:

- Recency
- Frequency
- Monetary Value
- Average Order Value
- Average Quantity

## Current Results

- Customers analyzed: 4,338
- Selected K-Means clusters: 2
- K-Means Silhouette Score: 0.9759
- DBSCAN clusters: 2
- DBSCAN noise points: 69
- Selected DBSCAN eps: 0.6
- PCA variance explained: 72.39%

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Google Colab

## Files

- `Project3_Customer_Clustering.ipynb` – Complete clustering implementation
