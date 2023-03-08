from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list):
        expiration_date = []
        manufacturing_date = []
        current_date = str(datetime.now())
        counter = Counter()

        for info in list:
            manufacturing_date.append(info["data_de_fabricacao"])
            if info["data_de_validade"] > current_date:
                expiration_date.append(info["data_de_validade"])
            counter[info["nome_da_empresa"]] += 1

        manufacturing_date.sort()
        expiration_date.sort()

        return (
            f"Data de fabricação mais antiga: {manufacturing_date[0]}\n"
            f"Data de validade mais próxima: {expiration_date[0]}\n"
            f"Empresa com mais produtos: {counter.most_common()[0][0]}"
        )
