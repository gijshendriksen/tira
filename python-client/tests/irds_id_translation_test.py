from tira.ir_datasets_util import translate_irds_id_to_tirex
from tira.third_party_integrations import ensure_pyterrier_is_loaded
import pyterrier as pt

ensure_pyterrier_is_loaded()

def test_for_tirex_id_robust04():
    expected = 'disks45-nocr-trec-robust-2004-20230209-training'
    actual = translate_irds_id_to_tirex( 'disks45-nocr-trec-robust-2004-20230209-training')
    
    assert expected == actual

def test_for_tirex_id_cw09_2014():
    expected = 'clueweb12-trec-web-2014-20230107-training'
    actual = translate_irds_id_to_tirex('clueweb12-trec-web-2014-20230107-training')
    
    assert expected == actual

def test_for_raw_string_robust04():
    expected = 'disks45-nocr-trec-robust-2004-20230209-training'
    actual = translate_irds_id_to_tirex('disks45/nocr/trec-robust-2004')
    
    assert expected == actual

def test_for_raw_string_cw09_2014():
    expected = 'clueweb12-trec-web-2014-20230107-training'
    actual = translate_irds_id_to_tirex('clueweb12/trec-web-2014')
    
    assert expected == actual

def test_for_pyterrier_dataset_robust04():
    expected = 'disks45-nocr-trec-robust-2004-20230209-training'
    actual = translate_irds_id_to_tirex(pt.get_dataset("irds:disks45/nocr/trec-robust-2004"))
    
    assert expected == actual

def test_for_pyterrier_dataset_cw09_2009():
    expected = 'clueweb09-en-trec-web-2009-20230107-training'
    actual = translate_irds_id_to_tirex(pt.get_dataset("irds:clueweb09/en/trec-web-2009"))
    
    assert expected == actual
