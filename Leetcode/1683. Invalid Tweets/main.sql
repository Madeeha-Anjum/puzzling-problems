+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.


Find the IDs of the invalid tweets.
note: content characters > 15 is invalid


SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
 