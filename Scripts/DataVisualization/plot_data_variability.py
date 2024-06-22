import re
import pandas as pd
import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(os.getcwd())
plt.rcParams['font.family'] = 'sans-serif'
sns.set_theme()
import numpy as np
import scipy.stats as stats
from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Plot the used keywords and options of the given dataset')
    parser.add_argument('--dataset_type', type=str,
                        required=True)
    args = parser.parse_args()
    return args


def get_dataset_color(dataset_type):
    # Define colors based on dataset_type
    if dataset_type == "Brute-Force":
        return '#E7C2B6'
    elif dataset_type == "Rule-Based":
        return '#A9CBAB'
    elif dataset_type == "Manual-Based":
        return '#B9CCD9'
    else:
        return 'steelblue'


def vizualize_keyword_frequency(data, dataset_name, color, top_n=20):
   # Convert counts to percentages
    total = sum(data.values())
    percentages = {key: (value / total) * 100 for key, value in data.items()}

    # Sort keywords by percentage
    sorted_percentages = sorted(
        percentages.items(), key=lambda x: x[1], reverse=True)
    top_n_keywords = dict(sorted_percentages[:top_n])

    # Convert to pandas Series for easier plotting
    top_n_series = pd.Series(top_n_keywords)

    # Create a horizontal bar plot using Seaborn
    plt.figure(figsize=(10, 6))

    sns.barplot(x=top_n_series.values, y=top_n_series.index,
                orient='h', color=color)
    # Annotate each bar with its percentage value
    for i, v in enumerate(top_n_series.values):
        plt.text(v + 0.2, i, f'{v:.2f}%', va='center', fontsize=8)

    plt.xlim(0, 15)
    plt.xlabel('Frequency (%)', fontsize=14, labelpad=10)
    plt.ylabel('Keywords', fontsize=14, labelpad=14)
    plt.title(f'Frequency of top-20 Keywords ({dataset_name})', fontweight='bold', fontsize=16, pad=12)
    plt.show()


def vizualize_option_frequency(data, dataset_name, color):

    # Convert counts to percentages
    total = sum(data.values())
    percentages = {key: (value / total) * 100 for key, value in data.items()}
    percentages = dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))

    # Convert to pandas Series for easier plotting
    percentages_series = pd.Series(percentages)

    # Create a horizontal bar plot using Seaborn

    plt.figure(figsize=(10, 6))
    sns.barplot(x=percentages_series.values,
                y=percentages_series.index, orient='h', color=color)

    # Annotate each bar with its percentage value
    for i, v in enumerate(percentages_series.values):
        plt.text(v + 0.2, i, f'{v:.2f}%', va='center', fontsize=8)
    plt.xlabel('Frequency (%)', fontsize=14, labelpad=10)
    plt.ylabel('Options', fontsize=14, labelpad=14)
    plt.xlim(0, 50)

    plt.title(f'Frequency of Options ({dataset_name})', fontweight='bold', fontsize=16, pad=12)
    plt.show()


def plot_data_variability(dataset_type):
    dataset_statistics = {
        "keyword": {},
        "option": {}
    }
 
    dataset_path = os.path.join("Data", "Test", f"{dataset_type}.csv")
    df = pd.read_csv(dataset_path, sep='|')
    input_files = df['label'].to_list()
    for input_file in input_files:
        keywords, _ = OrcaInputFileManipulator.extract_keywords(input_file)
        try:
            keywords.remove('pal6')
        except:
            pass
        input_blocks, options, settings = OrcaInputFileManipulator.extract_input_blocks(
            input_file)
        for keyword in keywords:
            dataset_statistics["keyword"][keyword] = dataset_statistics["keyword"].get(
                keyword, 0) + 1
        for option in options:
            dataset_statistics["option"][option] = dataset_statistics["option"].get(
                option, 0) + 1
    # dataset_path = os.path.join("Data", "Generated", f"InputFiles{
    #                             re.sub('-', '', dataset_type)}")
    # input_files = [os.path.join(dataset_path, file)
    #                for file in os.listdir(dataset_path)]
    # for file in input_files:
    #     with open(file, 'r') as f:
    #         input_file = f.read()
    #         keywords, _ = OrcaInputFileManipulator.extract_keywords(input_file)
    #         try:
    #             keywords.remove('pal6')
    #         except:
    #             pass
    #         input_blocks, options, settings = OrcaInputFileManipulator.extract_input_blocks(
    #             input_file)
    #         for keyword in keywords:
    #             dataset_statistics["keyword"][keyword] = dataset_statistics["keyword"].get(
    #                 keyword, 0) + 1
    #         for option in options:
    #             dataset_statistics["option"][option] = dataset_statistics["option"].get(
    #                 option, 0) + 1
    color = get_dataset_color(dataset_type)
    vizualize_keyword_frequency(
        dataset_statistics['keyword'], dataset_type, color)
    vizualize_option_frequency(
        dataset_statistics['option'], dataset_type, color)

    # Calculate and print additional statistics
    unique_keywords = len(dataset_statistics['keyword'])
    total_keywords = sum(dataset_statistics['keyword'].values())

    mean_keyword_frequency = sum(dataset_statistics['keyword'].values()) / unique_keywords
    median_keyword_frequency = np.median(list(dataset_statistics['keyword'].values())) / unique_keywords 

    variance_keyword_frequency = sum((count - mean_keyword_frequency) ** 2 for count in dataset_statistics['keyword'].values()) / unique_keywords
    
    unique_options = len(dataset_statistics['option'])
    total_options = sum(dataset_statistics['keyword'].values())

    mean_option_frequency = sum(dataset_statistics['option'].values()) / unique_options
    variance_option_frequency = sum((count - mean_option_frequency) ** 2 for count in dataset_statistics['option'].values()) / unique_options
    median_option_frequency = np.median(list(dataset_statistics['option'].values())) / unique_options

    print(f"Total unique keywords: {unique_keywords}")
    print(f"Mean Frequency (%): {mean_keyword_frequency}")
    print(f"Median Frequency (%): {median_keyword_frequency}")
    print(f"Skewness: {stats.skew(list(dataset_statistics['keyword'].values()))}")

    print(f"Total unique options: {unique_options}")
    print(f"Mean Frequency (%): {mean_option_frequency}")
    print(f"Median Frequency (%): {median_option_frequency}")
    print(f"Skewness: {stats.skew(list(dataset_statistics['option'].values()))}")

if __name__ == "__main__":
    args = parse_arguments()
    plot_data_variability(args.dataset_type)
