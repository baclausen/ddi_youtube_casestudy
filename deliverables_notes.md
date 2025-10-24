# ddi_youtube_casestudy
ddi_youtube_casestudy

explains your project.  

Deliverables
Presentation
Your group will present your results to the class from a slide deck presentation. Your presentation should include:

•	Clearly state the goal of your project (what were you exploring?)

  The goal of this analysis is to identify **key engagement metrics** that drive a video’s likelihood to appear on YouTube’s U.S. trending list.

•	Clearly state a projected possible benefit to your inquiry

  ### Projected Benefit
Understanding these factors will help:
- **Content creators** optimize video performance for higher visibility.  
- **Marketers** tailor campaigns toward metrics that have the most influence on youtube videos going viral.  
- **Platform analysts** improve algorithms predicting video popularity.

•	Describe the data.

o	What features (columns) did you have to work with?

  category_id, views, likes, comment_count, days_before_viral (we added this column)

o	What features were you interested in?

  views, likes, comment_count, days_before_viral

o	Were the features numerical/categorical/text?

  - Numeric: views, likes, dislikes, comment_count

  - Categorical: category_id, channel_title, comments_disabled, ratings_disabled

  - Text: channel_title, tags, description

  - Datetime:  trending_date, publish_date,

o	Was a lot of data missing? If so, what did you do to handle it?

  No, just about 560 rows within the Description column were missing. We filled the missing data with "No Description Available"

o	How did features relate to each other, and the values that you were interested in?

  Views and Likes: Videos with more likes usually have more views, which means people enjoy and engage with popular videos.

  Views and Comment_Count: High comment counts often come with many views, which means more people watching leads to more discussion.

  Likes and Comment_Count: These two rise together, which means when people like a video, they are also more likely to comment.

  Category and Engagements: Some categories like Music or Entertainment naturally get higher engagement than others (like News).

  Publish Time and Trending Date: The time gap shows how fast a video gained traction, which means short gaps mean videos trend faster.

  Views and Days to Trend: Videos with high views in fewer days are likely to hit trending quickly.

o	Use plots to clearly communicate the data's story to stakeholders.

A repository including a README.md file
Your group repository will contain any notebooks and Python script files you used to complete your analysis. It should also contain a comprehensive README.md file. The README.md markdown file should be a written recap of the type of information you will be presenting. It may have sections that further explain your choices. Include any illustrations and graphics you will use in the presentation.
Readers of the file should be able to get a good sense of your project even without a presentation.
Create the readme and presentation as you go
It's a common habit that students wait to create their presentations and readme until the last possible moment.
You will have a significantly better experience if you craft these as you go.
