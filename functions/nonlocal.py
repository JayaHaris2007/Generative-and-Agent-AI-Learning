def update_order():
    chai_type = "masala"
    def kitchen():
        nonlocal chai_type
        chai_type = "ginger"

    kitchen()
    print("The updated chai type is:", chai_type)

update_order()
