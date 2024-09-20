# Python Challenge Repository

Welcome to the **Python Challenge** repository! This project consists of two Python scripting challenges: **PyBank** and **PyPoll**, which will test your ability to analyze data programmatically using Python. These challenges will give you hands-on experience with data manipulation, file I/O, and basic analytics in Python.

## Repository Structure

This repository contains the following key folders and files:

```
python-challenge/
│
├── PyBank/
│   ├── Resources/
│   │   └── budget_data.csv  # CSV file containing financial records for analysis
│   ├── analysis/
│   │   └── financial_analysis.txt  # Output file with financial analysis results
│   └── main.py  # Script for analyzing financial data
│
├── PyPoll/
│   ├── Resources/
│   │   └── election_data.csv  # CSV file containing election data for analysis
│   ├── analysis/
│   │   └── election_results.txt  # Output file with election results
│   └── main.py  # Script for analyzing election data
│
└── README.md  # This file
```

## Challenges Overview

### PyBank
In the **PyBank** challenge, you are tasked with analyzing a company's financial records. The dataset provided in `budget_data.csv` contains two columns:
- **Date**: The month of the record.
- **Profit/Losses**: The net profit or losses for that month.

Your Python script will compute the following:
1. Total number of months in the dataset.
2. Net total amount of Profit/Losses.
3. Average change in Profit/Losses over the entire period.
4. The greatest increase in profits (date and amount).
5. The greatest decrease in profits (date and amount).

Your final results will be displayed in the terminal and exported to a text file in the `analysis` folder.

### PyPoll
In the **PyPoll** challenge, you are given a dataset of election results in `election_data.csv` that includes:
- **Voter ID**: Unique identifier for each voter.
- **County**: The county in which the voter is registered.
- **Candidate**: The candidate the voter chose.

Your Python script will analyze this data to provide the following:
1. The total number of votes cast.
2. A list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on popular vote.

As with PyBank, your results will be printed to the terminal and saved to a text file in the `analysis` folder.

## Getting Started

### Prerequisites
Make sure you have Python installed on your system. This project assumes you have a working knowledge of:
- Python programming (including `csv`, `os`, and basic file handling)
- Git for version control

### Setup Instructions

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/python-challenge.git
   ```

2. Navigate to the folder of the challenge you'd like to work on (e.g., `PyBank` or `PyPoll`).

3. Ensure the data files are placed in the respective `Resources` folders. The `main.py` scripts are already set up to read from these locations.

4. Run the Python scripts using the following commands:

   For PyBank:
   ```
   python PyBank/main.py
   ```

   For PyPoll:
   ```
   python PyPoll/main.py
   ```

5. The analysis results will be displayed in your terminal and saved in the `analysis` folder as a text file.

### Expected Output

**PyBank Example:**

```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

**PyPoll Example:**

```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## Contributions
Feel free to fork this repository and create a pull request if you have any suggestions or improvements. All contributions are welcome!

## License
This project is licensed under the MIT License.

Happy coding!
