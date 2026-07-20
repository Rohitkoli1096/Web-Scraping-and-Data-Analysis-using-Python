# 🕸️ Web Scraping & Data Analysis using Python

<div align="center">

### An End-to-End Data Analytics Pipeline for Web Data Extraction, Processing, Visualization, and Insight Generation

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-success)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

# 📖 Overview

This project demonstrates a complete **end-to-end data analytics workflow** using Python, starting from web data extraction and ending with meaningful insights through visualization and sentiment analysis.

The project scrapes product information from the publicly available **Books to Scrape** website, transforms the raw HTML into structured datasets, performs data preprocessing, explores the data using statistical techniques, and visualizes trends through charts.

It serves as a practical introduction to **Web Scraping, Data Cleaning, Exploratory Data Analysis (EDA), Data Visualization, and Basic Sentiment Analysis**.

---

# 🎯 Project Objectives

- Extract structured data from web pages using Python
- Automate web scraping using BeautifulSoup
- Clean and preprocess raw datasets
- Perform Exploratory Data Analysis (EDA)
- Generate meaningful visualizations
- Classify product sentiment based on ratings
- Build a reusable data analytics workflow

---

# ✨ Features

- 🌐 Automated Web Scraping
- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Transformation
- 📈 Data Visualization
- 😊 Rating-Based Sentiment Analysis
- 📂 CSV Dataset Generation
- 📉 Statistical Insights

---

# 🏗️ Project Structure

```text
Web-Scraping-and-Data-Analysis-using-Python/
│
├── Task_1.py                  # Web Scraping
├── Task_2.py                  # Data Cleaning
├── Task_3.py                  # Data Visualization
├── Task_4.py                  # Sentiment Analysis
│
├── data/
│   ├── books_data.csv
│   └── books_with_sentiment.csv
│
├── outputs/
│   └── rating_chart.png
│
├── report.docx
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3 |
| Web Scraping | BeautifulSoup4, Requests |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Dataset | CSV |

---

# 🌐 Data Source

The project uses the publicly available practice website:

**Books to Scrape**

http://books.toscrape.com

This website is specifically designed for learning and practicing web scraping techniques.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Rohitkoli1096/Web-Scraping-and-Data-Analysis-using-Python.git

cd Web-Scraping-and-Data-Analysis-using-Python
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is unavailable:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

---

## 3️⃣ Execute the Project

```bash
python Task_1.py

python Task_2.py

python Task_3.py

python Task_4.py
```

---

# 🔄 Project Workflow

```text
Website
    │
    ▼
Web Scraping
    │
    ▼
Raw Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Processed Dataset
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Visualization
    │
    ▼
Sentiment Analysis
    │
    ▼
Insights & Reports
```

---

# 📊 Project Outputs

| File | Description |
|------|-------------|
| books_data.csv | Raw scraped dataset |
| books_with_sentiment.csv | Dataset with sentiment labels |
| rating_chart.png | Rating distribution visualization |
| report.docx | Project report |

---

# 📈 Key Insights

- Most books have ratings between **3 and 5 stars**.
- Positive sentiment accounts for the majority of products.
- Product prices vary significantly across different categories.
- Cleaned datasets are ready for further machine learning or business analysis.

---

# 😊 Sentiment Classification

| Rating | Sentiment |
|---------|-----------|
| ⭐⭐⭐⭐⭐ | Positive |
| ⭐⭐⭐⭐ | Positive |
| ⭐⭐⭐ | Neutral |
| ⭐⭐ | Negative |
| ⭐ | Negative |

---

# 🚧 Challenges

During development, the following challenges were addressed:

- Understanding website HTML structure
- Extracting nested HTML elements
- Cleaning currency symbols and unwanted characters
- Handling missing values
- Organizing scraped data into structured CSV files

---

# 🚀 Future Enhancements

- Selenium-based scraping for dynamic websites
- Scraping multiple pages automatically
- Export data to SQL databases
- Interactive dashboards using Power BI or Tableau
- Machine Learning-based sentiment analysis
- Scheduled automated scraping
- Data pipeline automation

---

# 📚 Learning Outcomes

This project helped strengthen practical knowledge in:

- Python Programming
- Web Scraping
- Data Cleaning
- Data Analysis
- Exploratory Data Analysis (EDA)
- Data Visualization
- Working with CSV datasets
- Python libraries for analytics

---

# 👨‍💻 Author

**Rohit Devidas Koli**

Computer Engineering Student

Python • Data Analytics • Web Scraping • Data Visualization • Machine Learning Enthusiast

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

Special thanks to **CodeAlpha** for providing the internship opportunity and project guidance that contributed to the development of this project.

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a Star!

Made with ❤️ by **Rohit Devidas Koli**

</div>
