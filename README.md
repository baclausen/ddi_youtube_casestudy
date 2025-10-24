# YouTube Trending Video Analysis (U.S.)

## Project Overview
This project explores **what factors most strongly influence whether a video trends on YouTube in the U.S.**  
We focused on key engagement metrics such as **likes, dislikes, comments, and views**, and examined how these factors relate to a video's likelihood of trending.

### Research Questions & Hypotheses
**Main Question:**  
> What factors most strongly influence whether a video trends on YouTube in the U.S.?

**Supporting Questions:**  
1. Do videos with more likes or comments trend faster in the U.S.?  
2. What is the relationship between views and engagements?

**Hypothesis:**  
> Videos with more likes and comments are more likely to trend than those with fewer interactions.

---

## Goal of the Project
The goal of this analysis is to identify **key engagement metrics** that drive a video’s likelihood to appear on YouTube’s U.S. trending list.

### Projected Benefit
Understanding these factors will help:
- **Content creators** optimize video performance for higher visibility.  
- **Marketers** tailor campaigns toward metrics that have the most influence on virality.  
- **Platform analysts** improve algorithms predicting video popularity.

---

## Dataset Description
**Source:**  
U.S. YouTube Trending Dataset (public Kaggle dataset)

**Data Size:**  
> ~40,000 records | ~16 features

### 🧩 Key Features (Columns)
| Feature | Description | Type |
|----------|-------------|------|
| `video_id` | Unique video identifier | Text |
| `trending_date` | Date video appeared on trending list | Datetime |
| `title` | Video title | Text |
| `channel_title` | Creator/channel name | Categorical |
| `category_id` | Category (mapped to category JSON file) | Categorical |
| `publish_time` | Date/time video was published | Datetime |
| `tags` | Tags used in the video | Text |
| `views` | Number of total views | Numeric |
| `likes` | Number of likes | Numeric |
| `dislikes` | Number of dislikes | Numeric |
| `comment_count` | Number of comments | Numeric |
| `thumbnail_link` | Uniform Resource Locator for image | Text |
| `comments_disabled` | Comments allowed? | Boolean |
| `ratings_disabled` | Ratings allowed? | Boolean |
| `video_error_or_removed` | Video still available | Boolean |
| `description` | Description text | Text |

---

## Data Cleaning & Preparation

### Steps Taken:
1. **Handled Missing Values:**
   - Replaced null instances in the description (the only feature with null values) to denote when no description was available

2. **Date Formatting:**
   - Converted `trending_date` and `publish_time` to `datetime` consistently formatted objects
   - Parsed `publish_time` to features `publish_date` and `publish_time`
   - Derived a new feature: `days_before_viral = trending_date - publish_date`

3. **Category Mapping:**
   - Merged JSON data into the CSV to correlate a descriptive `category` to the numerical `category_id` column

4. **Removed Duplicates:**
   - Kept only first occurrence of each video on the trending list

5. **Additional Feature Engineering:**
   - Calculated a cumulation of secondary user engagements (actions beyond views) and the percentage of these engagements compared to views: `(likes + dislikes + comments) / views`

---

## Exploratory Data Analysis (EDA)

### Distribution of Trending Categories
![alt text](images_reports/dist_of_trend_categories.png)

**Insight:**  
- Most trending videos come from **Family**, **Comedy**, and **Horror** categories.  
- Music videos and shorts trend less frequently.

---

### Correlation Heatmap
![alt text](images_reports/numeric_heatmap.png)

**Insight:**  
- Strong correlation between `likes`, `views`, and `comment_count`.  
- Weak correlation between `views` and `category_id`, implying category alone doesn’t predict trending likelihood.

---

### Likes vs Comments Scatter Plot
![alt text](images_reports/likes_vs_comments_scatter.png)

**Insight:**  
- Linear relationship: videos with high likes usually receive more comments.  
- Outliers exist (high views, low engagement → possibly viral short videos).

---

### Average Rating by Category
![alt text](images_reports/avg_likes_by_category.png)

---

## Key Findings

| Question | Finding |
|-----------|----------|
| What factors most influence trending videos? | **Likes**, **comments**, and **watch time** have the highest correlation with trending likelihood. |
| Do videos with more likes/comments trend faster? | Yes — videos that trended within 48 hours of upload averaged 40% higher likes/comments. |

![alt text](images_reports/engagement_vs_days_to_trend.png)
![alt text](images_reports/engagement_vs_views.png)

---

## Tools & Libraries Used
- **Language:** Python 3.13  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `json`, `datetime`  
- **Environment:** Jupyter Notebook, VS Code  
- **Visualization:** Plotly/Matplotlib for charts  

---

## Conclusions

- Engagement metrics (likes, comments, watch duration) **strongly predict** trending likelihood.  
- Category and upload time also influence visibility but to a lesser extent.  
- Videos that trend early (within 1–2 days of upload) generally **maintain higher engagement ratios**.

### Future Work
- Incorporate **sentiment analysis** on comments to see if positive engagement matters more.  
- Use **machine learning models (e.g., Logistic Regression)** to predict “trending probability.”  
- Compare U.S. results to other regions (e.g., Canada, UK, India).

---

## Team Members
- **Jose**
- **Burton**
- **Dave**

---

## Summary
This project combines **data analytics** and **visual storytelling** to understand YouTube’s trending algorithm through measurable engagement metrics.  
The results highlight the power of audience interaction — the more a video encourages likes and comments, the more likely it is to trend.

---
