import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

stopwords = set(STOPWORDS)

date_pattern = re.compile(r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}$')

word_counts_by_year = {}
current_year = None
for entry in articles:
    if date_pattern.match(entry):
        current_year = entry.split()[-1]  
        if current_year not in word_counts_by_year:
            word_counts_by_year[current_year] = Counter()
    elif current_year:
        words = [word.lower() for word in re.findall(r'\w+', entry) if word.lower() not in stopwords]
        word_counts_by_year[current_year].update(words)

all_words = Counter()
for year, word_counts in word_counts_by_year.items():
    all_words.update(word_counts)

top_words = [word for word, _ in all_words.most_common(10)]

frequency_matrix = {word: [] for word in top_words}
years = sorted(word_counts_by_year.keys())

for year in years:
    for word in top_words:
        frequency_matrix[word].append(word_counts_by_year[year][word])

plt.figure(figsize=(15, 8))

for word, frequencies in frequency_matrix.items():
    plt.plot(years, frequencies, label=word)

plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Top 10 Words Frequency Over Years')
plt.xticks(rotation=45, ha='right')
plt.legend(title="Words")
plt.tight_layout()
plt.show()
