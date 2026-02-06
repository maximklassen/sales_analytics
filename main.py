from analyzer import SalesAnalyzer
from algorithms import (
    compare_sorting_performance,
    compare_search_performance
)

def main():
    print("\033[33m\033[1m== Sales Analytics Platform ==\033[0m\n")
    print("Beginn...")

    analyzer = SalesAnalyzer("data/sales_data.csv")

    print("- Daten werden geladen...")
    analyzer.load_data()

    print("- Datenbereinigung...")
    analyzer.clean_data()

    print("- Der bereinigte Datensatz wird exportiert...")
    analyzer.export_clean_data("data/sales_clean.csv")

    print("- Berechnung von Analysen...")
    total_revenue = analyzer.total_revenue()
    aov = analyzer.average_order_value()
    customers = analyzer.customer_count()

    print(f"\n  \033[34mGesamtumsatz:\033[0m {total_revenue:.2f}")
    print(f"  \033[34mDurchschnittlicher Bestellwert:\033[0m {aov:.2f}")
    print(f"  \033[34mKundenzahl:\033[0m {customers}")

    print("\n- Zusammenfassenden Bericht wird generiert...")
    analyzer.generate_summary_report("output/summary_report.txt")

    print("- Export von Top-Kunden...")
    analyzer.export_top_customers("output/top_customers.csv")

    print("- Visualisierungen werden erstellt...")
    analyzer.plot_revenue_by_category(
        "output/figures/revenue_by_category.png"
    )
    analyzer.plot_monthly_revenue(
        "output/figures/monthly_revenue.png"
    )
    analyzer.plot_order_amount_distribution(
        "output/figures/order_distribution.png"
    )

    print("\n\033[32mProjekt erfolgreich abgeschlossen\033[0m")

if __name__ == "__main__":
    main()