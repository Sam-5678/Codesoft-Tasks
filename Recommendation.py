import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item rating data
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    # Movie ratings
    'The Matrix': [5, 4, 4, 3, 5],
    'Inception': [4, 5, 3, 2, 5],
    'Titanic': [1, 2, 5, 4, 1],
    'The Notebook': [1, 1, 0, 5, 1],
    'Avengers': [5, 5, 3, 2, 4],
    'Iron Man': [5, 4, 0, 1, 4],

    # Book ratings
    'Harry Potter': [5, 0, 4, 3, 5],
    'The Alchemist': [4, 5, 0, 2, 4],
    'Atomic Habits': [5, 5, 3, 0, 4],
    'To Kill a Mockingbird': [0, 4, 3, 5, 4],

    # Product ratings
    'iPhone': [5, 5, 4, 3, 5],
    'Samsung Galaxy': [4, 4, 0, 2, 4],
    'MacBook Pro': [5, 0, 3, 3, 5],
    'AirPods': [5, 5, 3, 2, 4],
    'Smartwatch': [0, 4, 0, 3, 4],
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('User', inplace=True)

# Similarity between users
user_similarity = cosine_similarity(df)
user_similarity_df = pd.DataFrame(user_similarity, index=df.index, columns=df.index)

# Function to get top similar users
def get_top_similar_users(target_user, top_n=2):
    if target_user not in df.index:
        return []
    sim_scores = user_similarity_df[target_user].drop(target_user)
    top_users = sim_scores.sort_values(ascending=False).head(top_n).index
    return top_users

# Recommend items user hasn't rated but similar users did
def recommend_items(user, category_prefix, top_n=2):
    if user not in df.index:
        return "User not found."

    similar_users = get_top_similar_users(user, top_n)
    user_ratings = df.loc[user]
    recommendations = {}

    # Filter columns by category
    items = [col for col in df.columns if category_prefix.lower() in col.lower()]

    for item in items:
        if pd.isna(user_ratings[item]) or user_ratings[item] == 0:
            score = 0
            count = 0
            for sim_user in similar_users:
                rating = df.loc[sim_user, item]
                if rating > 0:
                    score += rating
                    count += 1
            if count > 0:
                recommendations[item] = score / count

    if not recommendations:
        return "No recommendations found."

    # Sort by predicted score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:5]

# Select category
def get_category_prefix(category):
    if category == "movies":
        return ""
    elif category == "books":
        return "Harry|Alchemist|Atomic|Mockingbird"
    elif category == "products":
        return "iPhone|Samsung|MacBook|AirPods|Smartwatch"
    else:
        return ""

# Get user input
user_input = input("Enter your user (User1, User2, ...): ")
print("Choose category to get recommendations:\n1. movies\n2. books\n3. products")
category_input = input("Enter category: ").strip().lower()

# Get appropriate items
if category_input == "movies":
    result = recommend_items(user_input, "", top_n=2)
elif category_input == "books":
    book_columns = ['Harry Potter', 'The Alchemist', 'Atomic Habits', 'To Kill a Mockingbird']
    df_books = df[book_columns]
    result = recommend_items(user_input, "Harry|Alchemist|Atomic|Mockingbird", top_n=2)
elif category_input == "products":
    product_columns = ['iPhone', 'Samsung Galaxy', 'MacBook Pro', 'AirPods', 'Smartwatch']
    df_products = df[product_columns]
    result = recommend_items(user_input, "iPhone|Samsung|MacBook|AirPods|Smartwatch", top_n=2)
else:
    result = "Invalid category."

# Output
print("\nTop Recommendations:")
print(result)
