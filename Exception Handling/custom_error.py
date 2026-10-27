def bmw_model(model):
    if model not in ["M8", "M5", "M4", "M3", "M2", "XM", "X5M"]:
        raise ValueError("That model is not Supported...  (Sorry)")

    print("Your Model Available..")


bmw_model("M6")