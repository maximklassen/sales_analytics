from analyzer import SalesAnalyzer

def main():
    print("== Sales Analytics ==")
    
    analyzer = SalesAnalyzer("data/sales_data.csv")

    analyzer.load_data()
    analyzer.clean_data()
    analyzer.export_clean_data("data/sales_clean.csv")

    print("Data cleaned and exported successfully")

if __name__ == "__main__":
    main()