Overview

This Python project fetches research papers based on a user-specified query using the PubMed API. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and outputs the results as a CSV file.

Features
Fetches research papers using PubMed's full query syntax.

Identifies company-affiliated authors and non-academic authors.

Returns results in a CSV format with fields:

PubmedID: Unique identifier for the paper.

Title: Title of the paper.

Publication Date: Date the paper was published.

Non-academic Author(s): Names of authors affiliated with non-academic institutions.

Company Affiliation(s): Names of pharmaceutical/biotech companies.

Corresponding Author Email: Email address of the corresponding author.

Command-line interface (CLI) with options:

-h or --help: Display usage instructions.

-d or --debug: Print debug information during execution.

-f or --file: Specify the filename to save results (default is console output).

Installation

Prerequisites

Python >=3.13

Poetry for dependency management

Git for version control
Setup

Clone the repository and install dependencies:
# Clone the repository
git clone https://github.com/yourusername/research-paper-fetcher.git
cd research-paper-fetcher

# Install dependencies
poetry install
Usage

Run the CLI tool to fetch research papers:
example
poetry run get-papers-list "cancer treatment AND pharma"
To save the results to a file:
poetry run get-papers-list "cancer treatment" --file results.csv

To enable debugging:
poetry run get-papers-list "cancer treatment" --debug

CODE STRUCTURE
research-paper-fetcher/
│── src/
│   ├── my_project/
│   │   ├── __init__.py
│   │   ├── cli.py        # Command-line interface
│   │   ├── fetcher.py    # API call and data processing
│   │   ├── utils.py      # Helper functions
│── tests/                # Unit tests
│── pyproject.toml        # Poetry configuration
│── README.md             # Documentation
Development

Running Tests

To run unit tests:
poetry running pytest

