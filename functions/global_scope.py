chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "ginger"

    kitchen()

front_desk()

print(f"Global chai_type after front_desk function: {chai_type}")