import matplotlib.pyplot as plt

hashtag_counts = {}
with open("./output/hashtag_count.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "\t" in line:
            hashtag, count = line.strip().split("\t")
            hashtag_counts[hashtag] = int(count)

# Sort the hashtags by count in descending order and take the top 10
top_10 = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Separate hashtags and counts
hashtags, counts = zip(*top_10)

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(hashtags[::-1], counts[::-1], color='skyblue')  # Reverse for descending display
plt.xlabel('Count')
plt.title('Top 10 Hashtags')
plt.tight_layout()
plt.savefig("./plots/top_10_hashtags.png", dpi=300, bbox_inches='tight')
plt.show()
        