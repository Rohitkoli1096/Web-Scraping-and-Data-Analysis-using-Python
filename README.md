# 🚀 Web Scraping and Data Analysis using Python

## 📌 Overview
This project demonstrates a complete **end-to-end data analytics pipeline** using Python.  
It includes web scraping, data preprocessing, exploratory data analysis (EDA), data visualization, and sentiment analysis.

The data is collected from a sample e-commerce website and transformed into structured datasets for analysis and insights.

---

## 🎯 Objectives
- Extract data from websites using web scraping  
- Perform data cleaning and preprocessing  
- Analyze dataset using EDA techniques  
- Visualize patterns using graphs  
- Apply sentiment analysis  

---

## 🛠️ Technologies Used
- Python  
- BeautifulSoup  
- Requests  
- Pandas  
- Matplotlib  

## 📂 Project Structure

```bash
Web-Scraping-and-Data-Analysis-using-Python/
│
├── Task_1.py              # Web Scraping
├── Task_2.py              # EDA + Data Cleaning
├── Task_3.py              # Data Visualization
├── Task_4.py              # Sentiment Analysis
│
├── data/                  # Dataset files
│   ├── books_data.csv
│   ├── cleaned_books_data.csv
│   ├── books_with_sentiment.csv
│
├── outputs/               # Graphs / charts
│   ├── rating_chart.png
│
├── report.docx            # Final report (Word file)
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
```


---

## 🔍 Data Source
- http://books.toscrape.com  

---

## ⚙️ How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Rohitkoli1096/Web-Scraping-and-Data-Analysis-using-Python.git
cd Web-Scraping-and-Data-Analysis-using-Python
```

### 2️⃣ Install Dependencies
```bash
pip3 install requests beautifulsoup4 pandas matplotlib
```

### 3️⃣ Run Project
```bash
python3 Task_1.py
python3 Task_2.py
python3 Task_3.py
python3 Task_4.py
```

---

## 📊 Outputs
- 📄 **books_data.csv** → Raw scraped dataset  
- 📄 **books_with_sentiment.csv** → Dataset with sentiment classification  
- 📈 **rating_chart.png** → Visualization of rating distribution  

---

## 📈 Key Insights
- Most products have ratings between 3 to 5  
- Positive sentiment dominates the dataset  
- Price distribution varies across products  

---

## 😊 Sentiment Analysis Logic
- ⭐ 4–5 → Positive  
- ⭐ 3 → Neutral  
- ⭐ 1–2 → Negative  

---

## ⚠️ Challenges Faced
- Handling HTML structure  
- Cleaning special characters (currency symbols)  
- Managing Python environment setup  

---

## 🔮 Future Improvements
- Use Selenium for dynamic websites  
- Scrape real-world e-commerce platforms  
- Apply machine learning for sentiment analysis  
- Build interactive dashboards  

---

## 👨‍💻 Author
**Rohit Koli**  
CodeAlpha Internship  

---

## 📜 License
MIT License  

---

## ⭐ Acknowledgement
Thanks to CodeAlpha for providing this internship opportunity.
