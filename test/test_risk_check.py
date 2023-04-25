from main import customer_id_count

def test_count_return():
    test_ids = [
        "1234",
        "1234", 
        "1234", 
        "47236", 
        "83183", 
        "37827"
        ] # 4
    
    assert customer_id_count(test_ids) == 4
    
    
    