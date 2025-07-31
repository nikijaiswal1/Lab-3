records = [
    {'name': "rice", "price": 120, "category": "grocery"},
    {'name': "sugar", "price": 220, "category": "grocery"},
    {'name': "wheat", "price": 320, "category": "grocery"},
    {'name': "rcereal", "price": 420, "category": "grocery"},
]

with open("grocery.txt", "w") as f:
    f.write("ID NAME PRICE CATEGORY\n")
    for idx, rec in enumerate(records, start=1):
        f.write(f"{idx} {rec['name']} {rec['price']} {rec['category']}\n")

read_records = []
with open("grocery.txt", "r") as f:
    next(f)  # Skip the header line
    for line in f:
        parts = line.strip().split()
        read_records.append({
            'name': parts[1],
            'price': int(parts[2]),
            'category': parts[3]
        })

print("Reconstructed Records:")
for rec in read_records:
    print(rec)
