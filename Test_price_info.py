import price_info as price

def test_cost_of_fruit():
    expected_result=12.0
    test_result=price.cost_of_fruits(price.price_list['apple'],10)
    assert(test_result==expected_result)
    
def test_total_cost_shopping():
    expected_result=46.75
    assert(price.total_cost_shopping()==expected_result)


