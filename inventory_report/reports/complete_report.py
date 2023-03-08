from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_result = super().generate(list)
        companies_list = []
        companies = Counter(companies_list)
        string = ""

        for product in list:
            companies_list.append(product["nome_da_empresa"])

        for company in companies.most_common():
            string += f'- {company[0]}: {company[1]}\n'

        return (
            f"{simple_result}\n"
            f"Produtos estocados por empresa:\n"
            f"{string}s"
        )
