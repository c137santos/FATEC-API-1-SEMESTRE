from regra_de_negocio.global_settings import read_global_settings   


def test_pega_as_global_settings():
    info_settings = read_global_settings()
    assert info_settings == {"quantidade_sprint": 4, "dias_sprint": 15}
