from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from PIL import Image

titles_by_year = {}
current_year = None
for article in articles:
    if 'Editorial Board' in article:
        continue
    if article.startswith(('January', 'February', 'March', 'April', 'May', 'June', 
                            'July', 'August', 'September', 'October', 'November', 'December')):
        current_year = article.split()[-1]
    elif current_year:
        titles_by_year.setdefault(current_year, []).append(article)
for year, titles in titles_by_year.items():
    text = " ".join(titles)
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis", 
        contour_width=1, 
        contour_color="black",
        max_words=200, 
        max_font_size=120, 
        random_state=42,  
    ).generate(text)

    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud for {year}", fontsize=18)
    plt.tight_layout()
    plt.show()
