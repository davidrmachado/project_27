from inventory_report.inventory.product import Product

aviso_segurança = "mantenha fora do alcance das crianças"


def test_cria_produto():
    product = Product(
        1,
        "suco",
        "sucos & co",
        "01/12/2022",
        "10/01/2023",
        12345678,
        aviso_segurança,
    )

    assert product.id == 1
    assert product.nome_do_produto == "suco"
    assert product.nome_da_empresa == "sucos & co"
    assert product.data_de_fabricacao == "01/12/2022"
    assert product.data_de_validade == "10/01/2023"
    assert product.numero_de_serie == 12345678
    assert product.instrucoes_de_armazenamento == aviso_segurança
