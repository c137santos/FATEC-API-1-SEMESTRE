from global_settings import read_global_settings, edit_global_settings

def test_pega_as_global_settings():
    info_settings = read_global_settings()
    assert info_settings == {'quantidade_sprint': 4, 'dias_sprint': 15}
    

def test_altera_global_setings():
    edit_global_settings(quantidade_sprint=2, dias_sprint=10) 
    info_settings = read_global_settings()
    assert info_settings == {'quantidade_sprint': 2, 'dias_sprint': 10}
