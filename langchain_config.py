import re
from collections import Counter


STOP_WORDS = {
    "the", "a", "an", "and", "or", "but",
    "to", "of", "in", "on", "for", "with",
    "at", "by", "from", "is", "are", "was",
    "were", "this", "that", "has", "have",
    "had", "will", "it", "its"
}


def create_news_summary(query, articles):

    if not articles:
        return "No articles found."

    sentences = []

    for article in articles:

        title = article.get("title", "")

        description = article.get("description", "")

        if title:
            sentences.append(title)

        if description:

            parts = re.split(
                r'(?<=[.!?])\s+',
                description
            )

            sentences.extend(parts)

    words = re.findall(
        r'\b[a-zA-Z]{3,}\b',
        " ".join(sentences).lower()
    )

    frequency = Counter(
        word for word in words
        if word not in STOP_WORDS
    )

    scored = []

    for sentence in sentences:

        tokens = re.findall(
            r'\b[a-zA-Z]{3,}\b',
            sentence.lower()
        )

        score = sum(
            frequency[word]
            for word in tokens
        )

        if len(sentence) > 30:

            scored.append(
                (score, sentence)
            )

    scored.sort(
        reverse=True
    )

    selected = []

    for score, sentence in scored:

        if sentence not in selected:

            selected.append(sentence)

        if len(selected) == 5:
            break

    result = f"## News Summary: {query}\n\n"

    for sentence in selected:

        result += "- " + sentence + "\n"

    result += (
        "\n### Note\n"
        "This is a basic extractive summary created locally "
        "using Python. Please verify information from original articles."
    )

    return result