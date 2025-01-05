import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

stopwords = set(STOPWORDS)

date_pattern = re.compile(r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}$')

word_counts_by_month = {}
current_month = None
for entry in articles:
    if date_pattern.match(entry):
        current_month = entry
        word_counts_by_month[current_month] = Counter()
    elif current_month:
        words = [word.lower() for word in re.findall(r'\w+', entry) if word.lower() not in stopwords]
        word_counts_by_month[current_month].update(words)

all_words = Counter()
for month, word_counts in word_counts_by_month.items():
    all_words.update(word_counts)

top_words = [word for word, _ in all_words.most_common(10)]

frequency_matrix = {word: [] for word in top_words}
months = list(word_counts_by_month.keys())

for month in months:
    for word in top_words:
        frequency_matrix[word].append(word_counts_by_month[month][word])

plt.figure(figsize=(15, 8))

for word, frequencies in frequency_matrix.items():
    plt.plot(months, frequencies, label=word)

january_indices = [i for i, month in enumerate(months) if month.startswith("January")]
january_labels = [months[i] for i in january_indices]

plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Top 10 Words Frequency Over Time')
plt.xticks(ticks=january_indices, labels=january_labels, rotation=45, ha='right')
plt.legend(title="Words")
plt.tight_layout()
plt.show()
