# Movies Recommender System

## Basic Idea of Movie Recommender System

While working on data, it is important to know how to use data. So, here in this case, what I intent to do is, find the Keywords of each movie like, title, genres, overview, main keywords, cast, crew and even more if needed. After having those keywords in single array, it can be drawn into vectors for machine to understand and then finding the minimum distance between movies and least the distance more the similarity between the movies.

## Data Source

Using the Kaggle data set of TMDB 5000 Movie Dataset for working on this project.

Source Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Working on Code

Converting data into vectors using CountVectorizer tool under scikit-learn library. Then, converting the words into its root form, removing prefix or suffix using PorterStemmer tool.
Now, the most important function of Movies Recommender system is finding distance between each vector. Here we have multiple options to do so, where using Euclidean method can be used but it gives less accuracy. So, using Cosine Similarity in this so that we get higher accuracy.
Difference between Euclidean and Cosine SimilarityData ModellingModel is working perfectlyWorking on Implementing Code on website
Now, our model is done and it's time to implement it on Heroku website using streamlit library.

## Result

https://miro.medium.com/max/1400/1*-ufILM9FuLKCBFIofjvjWw.png

Here is the look of the Movie Recommender System.
Link for the app: https://bhupesh-mrs.herokuapp.com/

## Conclusion

I had learned alot through the process and it had made me even more curios of working on more projects. I had gone through process like, data cleaning, data analysis, data modelling, deployment.
Have any query, contact me via email: bhupeshrathore932@gmail.com
