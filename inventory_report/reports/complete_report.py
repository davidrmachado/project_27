from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        simple_result = SimpleReport.generate(products)
        string = ""
        companies = Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common()

        for company in companies:
            string += f'- {company[0]}: {company[1]}\n'

        return (
            f"{simple_result}\n"
            f"Produtos estocados por empresa:\n"
            f"{string}"
        )
