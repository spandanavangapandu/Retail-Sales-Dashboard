# 📊 RetailScope: Visualizing Sales Performance

**RetailScope** is a Tableau-powered business intelligence dashboard that visualizes and analyzes sales and profitability metrics from a retail Superstore dataset. This project highlights regional sales, category-wise profitability, and temporal sales trends to help stakeholders make informed decisions.

---

## 🚀 Features

- **Sales Breakdown by Region**  
  Compare total revenue across four key U.S. regions.

- **Profit by Product Category**  
  Identify which product categories yield the highest margins.

- **Segment-wise Profit Margin**  
  Analyze profitability per customer segment: Home Office, Corporate, and Consumer.

- **Sales by State (Geo Map)**  
  Explore U.S. state-wise sales performance using a gradient-filled map.

- **Monthly Sales Trend Analysis**  
  Detect seasonal spikes and dips using a clean, interactive line chart.

---

## 📁 Project Structure

```
RetailScope/
│
├── data/
│   ├── Superstore.csv              # Raw dataset
│   └── Cleaned_Superstore.csv      # Cleaned and formatted for analysis
│
├── dashboard/
│   ├── Retail Sales Dashboard.twb  # Tableau workbook
│   └── Dashboardvisual.png     # Exported visual for documentation
│
├── scripts/
│   └── RetailScope_Analysis.py     # Data processing using pandas
│
└── README.md
```

---

## 🛠 Tools Used

- **Tableau Desktop Public Edition** – Visualization and dashboarding
- **Python (pandas)** – Data cleaning & preprocessing
- **CSV Files** – Source data
- **Mapbox + Tableau** – Geo visualizations

---

## ⚙️ Getting Started

1. Clone this repository.
2. Open `Retail Sales Dashboard.twb` in Tableau Desktop.
3. If prompted, reconnect the data source to `Cleaned_Superstore.csv`.
4. Explore the interactive filters and visuals.

---

## 📸 Preview

![Dashboard Visual](dashboard/Dashboardvisual.png)

---

## 🧹 Data Cleaning

Data was cleaned using `RetailScope_Analysis.py` to:
- Fix date formats
- Remove nulls
- Ensure numerical consistency
- Export a clean dataset for Tableau (`Cleaned_Superstore.csv`)

---

## 📌 Notes

- Tableau file paths are relative; ensure your dataset is in the correct folder.
- Data is anonymized and suitable for academic or demo use.

---

## 🧑‍💻 Author

SPANDANA VANGAPANDU

---

## 📄 License

This project is open-source under the MIT License.
