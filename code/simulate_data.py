import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Parameters
NUM_RECORDS = 1000
START_DATE = '2022-01-01'
END_DATE = '2022-12-31'

# Generate dates
dates = pd.date_range(start=START_DATE, end=END_DATE, periods=NUM_RECORDS)
# dates = np.random.choice(dates, replace=True, size=NUM_RECORDS)

# Generate happiness levels
def simulate_happiness(n):
    x = np.linspace(0, 12, n)
    noise = np.random.normal(0, 1, n)
    y = 1.5 + 0.5 * x + np.sin(x) + noise
    y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 4 + 1
    return y

happiness_levels = simulate_happiness(NUM_RECORDS).astype(int)

# Generate Age Groups
def generate_age_groups(n):
    age_groups = ['<30', '31-40', '41-50', '51-60', '>60']
    group_indices = np.random.choice(len(age_groups), size=n)
    groups = [age_groups[i] for i in group_indices]
    return groups

## Function to generate full sentences for feedback
def generate_feedback_text(happiness_level):
    if happiness_level == 1:
        return fake.sentence(nb_words=15, ext_word_list=['I', 'am', 'very', 'unhappy', 'with', 'my', 'job.', 'The', 'work', 'environment', 'is', 'stressful', 'and', 'disorganized.'])
    elif happiness_level == 2:
        return fake.sentence(nb_words=15, ext_word_list=['I', 'am', 'dissatisfied', 'with', 'my', 'job.', 'There', 'are', 'many', 'things', 'that', 'could', 'be', 'improved.'])
    elif happiness_level == 3:
        return fake.sentence(nb_words=15, ext_word_list=['I', 'feel', 'neutral', 'about', 'my', 'job.', 'It', 'has', 'its', 'ups', 'and', 'downs.'])
    elif happiness_level == 4:
        return fake.sentence(nb_words=15, ext_word_list=['I', 'am', 'satisfied', 'with', 'my', 'job.', 'Most', 'things', 'are', 'going', 'well.'])
    elif happiness_level == 5:
        return fake.sentence(nb_words=15, ext_word_list=['I', 'am', 'very', 'happy', 'with', 'my', 'job.', 'The', 'work', 'environment', 'is', 'excellent', 'and', 'supportive.'])

# Generate feedback texts with full sentences
feedback_texts_full = [generate_feedback_text(level) for level in happiness_levels]

# Create new DataFrame with full sentences
df_full_sentences = pd.DataFrame({
    'Date': dates,
    'Age_Group': generate_age_groups(NUM_RECORDS),
    'Happiness_Level': happiness_levels,
    'Feedback': feedback_texts_full
})


# Save to new CSV
file_path_full_sentences = "/Users/rkruse/Git/DashBoard/data/simulated_data.csv"
df_full_sentences.to_csv(file_path_full_sentences, index=False)
