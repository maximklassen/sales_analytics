from analyzer import SalesAnalyzer
from algorithms import (
    compare_sorting_performance,
    compare_search_performance
)

def main():
    analyzer = SalesAnalyzer("data/sales_data.csv")
    analyzer.load_data()
    analyzer.clean_data()

    analyzer.export_clean_data("data/sales_clean.csv")

    analyzer.generate_summary_report(
        "output/summary_report.txt"
    )

    analyzer.export_top_customers(
        "output/top_customers.csv"
    )

    analyzer.plot_revenue_by_category(
        "output/figures/revenue_by_category.png"
    )

    analyzer.plot_monthly_revenue(
        "output/figures/monthly_revenue.png"
    )

    analyzer.plot_order_amount_distribution(
        "output/figures/order_distribution.png"
    )

    print("Projekt erfolgreich abgeschlossen")

if __name__ == "__main__":
    main()