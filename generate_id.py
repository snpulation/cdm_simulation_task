
def generate_id(num = 1):
    return [f"ID_{str(i).zfill(3)}" for i in range(1, num+1)]