

# E-Commerce Data Generator

## Overview

This project provides a  script utilizing the LangChain framework to parse, understand, and enrich e-commerce product data from various formats (CSV, XLSX, XML) and output the enriched data in a structured JSON format. The goal is to facilitate the creation of a well-organized, structured database suitable for e-commerce systems.

## Features

- **Data Parsing**: Read data from multiple formats, including CSV, XLSX, and XML files.
- **Data Enrichment**: Utilize LangChain and OpenAI for natural language understanding to enrich product descriptions.
- **Structured Output**: Generate structured JSON output that mirrors a proposed database schema for e-commerce platforms.
- **Scalability**: Designed to handle different data sizes and formats, ensuring the script is adaptable for various e-commerce data sets.
- **Error Handling**: Implements robust error handling to manage common anomalies found in unstructured data files.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- pandas
- openpyxl (for processing `.xlsx` files)
- An OpenAI API key for utilizing LangChain and OpenAI services.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://your-repository-link.git
    cd your-repository-directory
    ```

2. **Set Up a Virtual Environment** (Optional but recommended)

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install pandas openpyxl langchain-openai
    ```

4. **Configure OpenAI API Key**

    Set your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your_api_key_here'  # On Windows use `set` instead of `export`
    ```

## Usage

To use the script, follow these instructions:

1. **Prepare Your Data Files**

    Place your CSV, XLSX, and XML files within the `./CSV` directory of the project.

2. **Run the Script**

    ```bash
    python3 apx.py
    ```

    This will process all supported files in the `./CSV` directory, enrich the data, and output corresponding JSON files in the same directory.

## Output Format

The script outputs JSON files with enriched data. The structure is tailored to fit an e-commerce platform's requirements, including detailed product information and metadata. Here's a sample of the JSON structure:

```json
{
  "imports": {
    "EAN": "4049441018409",
    "rrp": "499.99",
    ...
  },
  "mp_partner": {
    "id": 736,
    ...
  },
  ...
}
```

## Contributing

Contributions to this project are welcome. Please follow the conventional commit messages and ensure your code adheres to the project's coding standards.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please contact the project maintainers

---

**Note:** You'll need to replace placeholders like `https://your-repository-link.git`, `your-repository-directory`, and `your_api_key_here` with actual values relevant to your project.
