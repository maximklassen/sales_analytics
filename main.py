from analyzer import SalesAnalyzer
from algorithms import (
    compare_sorting_performance,
    compare_search_performance
)

def main():
    analyzer = SalesAnalyzer("data/sales_data.csv")
    analyzer.load_data()
    analyzer.clean_data()

    analyzer.plot_revenue_by_category(
        "output/figures/revenue_by_category.png"
    )

    analyzer.plot_monthly_revenue(
        "output/figures/monthly_revenue.png"
    )

    analyzer.plot_order_amount_distribution(
        "output/figures/order_distribution.png"
    )

    print("Visualizations created")
#    print("Sorting performance:", compare_sorting_performance())
#    print("Search performance:", compare_search_performance())

# def main():
#    print("== Sales Analytics ==")
#
#    analyzer = SalesAnalyzer("data/sales_data.csv")
#
#    analyzer.load_data()
#    analyzer.clean_data()
#    analyzer.export_clean_data("data/sales_clean.csv")
#
#    print("\n\033[33mGemeinsames Einkommen:\033[0m", analyzer.total_revenue())
#    print("\n\033[32mDurchschnittlicher Bestellwert:\033[0m", analyzer.average_order_value())
#    print("\n\033[34mKunden:\033[0m", analyzer.customer_count())
#    print("\n\033[35mTop-Kategorie:\033[0m\n", analyzer.revenue_by_category())
#    print("\n\033[36mWiederkaufrate:\033[0m", analyzer.repeat_customer_rate())

if __name__ == "__main__":
    main()