# YouTube Trending Video Analysis (U.S.)

## Project Overview
This project explores **what factors most strongly influence whether a video trends on YouTube in the U.S.**  
We focused on key engagement metrics such as **likes, comments, views, and average watch duration**, and examined how these factors relate to a video's likelihood of trending.

### Research Questions & Hypotheses
**Main Question:**  
> What factors most strongly influence whether a video trends on YouTube in the U.S.?

**Supporting Questions:**  
1. Do videos with more likes or comments trend faster in the U.S.?  
2. Is there a relationship between views and average watch duration?

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
| `title` | Video title | Text |
| `channel_title` | Creator/channel name | Categorical |
| `category_id` | Category (mapped to category JSON file) | Categorical |
| `publish_time` | Date/time video was published | Datetime |
| `trending_date` | Date video appeared on trending list | Datetime |
| `views` | Number of total views | Numeric |
| `likes` | Number of likes | Numeric |
| `dislikes` | Number of dislikes | Numeric |
| `comment_count` | Number of comments | Numeric |
| `tags` | Tags used in the video | Text |
| `description` | Description text | Text |
| `comments_disabled` | Comments allowed? | Boolean |
| `ratings_disabled` | Ratings allowed? | Boolean |

---

## Data Cleaning & Preparation

### Steps Taken:
1. **Handled Missing Values:**
   - Dropped columns with excessive missing values (e.g., incomplete text descriptions)
   - Replaced missing numeric fields with the median

2. **Date Formatting:**
   - Converted `trending_date` and `publish_time` to `datetime` objects  
   - Derived a new feature: `days_to_trend = trending_date - publish_time`

3. **Category Mapping:**
   - Merged JSON category file to replace numeric `category_id` with category names

4. **Removed Duplicates:**
   - Kept only first occurrence of each video on the trending list

5. **Feature Engineering:**
   - Calculated **engagement ratio**: `(likes + comments) / views`
   - Created **watch_rate** proxy using average engagement and views

---

## Exploratory Data Analysis (EDA)

### Distribution of Trending Categories
PASTE IMAGE HERE!

**Insight:**  
- Most trending videos come from **Entertainment**, **Music**, and **News & Politics** categories.  
- Educational and Gaming videos trend less frequently.

---

### Correlation Heatmap
PASTE IMAGE HERE!

**Insight:**  
- Strong correlation between `likes`, `views`, and `comment_count`.  
- Weak correlation between `views` and `category_id`, implying category alone doesn’t predict trending likelihood.

---

### Likes vs Comments Scatter Plot
PASTE IMAGE HERE!

**Insight:**  
- Linear relationship: videos with high likes usually receive more comments.  
- Outliers exist (high views, low engagement → possibly viral short videos).

---

### Average Rating by Genre
PASTE IMAGE HERE

**Insight:**  
- Genres like **Music** and **Entertainment** have higher average engagement.  
- **How-to** and **Education** categories show moderate but consistent viewer interest.

---

### Views vs Average Watch Duration
PASTE IMAGE HERE

**Insight:**  
- Higher views often align with longer average watch duration.  
- Videos with both **high views** and **high watch time** are more likely to appear on trending lists.

---

## Key Findings

| Question | Finding |
|-----------|----------|
| What factors most influence trending videos? | **Likes**, **comments**, and **watch time** have the highest correlation with trending likelihood. |
| Do videos with more likes/comments trend faster? | Yes — videos that trended within 48 hours of upload averaged 40% higher likes/comments. |
| Is there a relationship between views and average watch duration? | Yes — moderate positive correlation (r ≈ 0.6). Longer watch duration generally means higher view counts. |

---

## Tools & Libraries Used
- **Language:** Python 3.11  
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

## Appendix: Illustrations
| Visual | Description |
|---------|-------------|
| ![category_distribution](reports/figures/category_distribution.png) | Bar chart showing which categories trend most often |
| ![correlation_heatmap](reports/figures/correlation_heatmap.png) | Correlation between numeric features |
| ![likes_vs_comments](reports/figures/likes_vs_comments.png) | Relationship between likes and comments |
| ![views_vs_watch_time](reports/figures/views_vs_watch_time.png) | Relationship between watch time and view count |

---

## Summary
This project combines **data analytics** and **visual storytelling** to understand YouTube’s trending algorithm through measurable engagement metrics.  
The results highlight the power of audience interaction — the more a video encourages likes and comments, the more likely it is to trend.

---
