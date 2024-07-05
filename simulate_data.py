import numpy as np 
import pandas as pd 

def simulate(n):
    x = np.linspace(0, 12, n)
    noise = np.random.normal(0, 1, n)
    y = 1.5 + 0.5 * x + np.sin(x) + noise
    y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 4 + 1
    dates = pd.date_range(start='01-01-2022', periods=n, freq='D').strftime('%d-%m-%y')
    
    positive_words = read_words_from_file("/Users/rkruse/Git/DashBoard/data/opinion-lexicon-English/positive-words.txt")
    negative_words = read_words_from_file("/Users/rkruse/Git/DashBoard/data/opinion-lexicon-English/negative-words.txt")
    
    sampled_word_data = sample_words(positive_words, negative_words, n)
    groups = generate_age_groups(n)
    
    data = pd.DataFrame({'Date': dates, 'Glücklich': y, 'text': sampled_word_data, 'Alter': groups})
    return data

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return pd.Series(words)

def sample_words(positive_words, negative_words, n):
    word_data = pd.concat([negative_words, positive_words])
    sampled_word_data = word_data.sample(n)
    return sampled_word_data

def generate_age_groups(n):
    age_groups = ['<30', '31-40', '41-50', '51-60', '>60']
    group_indices = np.random.choice(len(age_groups), size=n)
    groups = [age_groups[i] for i in group_indices]
    return groups

# Simulate 1000 discrete values
happiness = simulate(1000)

# Save the simulated data in the folder 'data'
happiness.to_csv('/Users/rkruse/Git/DashBoard/data/simulated_data.csv', index=False)
