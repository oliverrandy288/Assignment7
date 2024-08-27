# Task 1: Keyword Highlighter
def highlight_keywords(reviews, keywords):
    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print("Highlighted Review:", highlighted_review)

# Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0

    for review in reviews:
        words = review.lower().split()
        positive_count = sum(word in positive_words for word in words)
        negative_count = sum(word in negative_words for word in words)
        
        total_positive += positive_count
        total_negative += negative_count

    return total_positive, total_negative

# Task 3: Review Summary
def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    summary = review[:max_length].rsplit(' ', 1)[0]  # Split by the last space within the limit
    return summary + "…"

# Task 4: Input Length Validator
def input_length_validator():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name must be at least 2 characters long.")
    else:
        print("Names are valid.")

# Define the data
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Execute tasks
print("Task 1: Keyword Highlighter")
highlight_keywords(reviews, keywords)

print("\nTask 2: Sentiment Tally")
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print(f"Total positive words: {positive_count}")
print(f"Total negative words: {negative_count}")

print("\nTask 3: Review Summary")
for review in reviews:
    print("Review Summary:", create_summary(review))

print("\nTask 4: Input Length Validator")
input_length_validator()
