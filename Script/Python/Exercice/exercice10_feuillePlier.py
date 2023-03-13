papier_mm = 0.1
pliage = 0

while papier_mm < 400000:
    pliage = pliage+1
    papier_mm = papier_mm *2
    print(f"après {pliage} pliage, nous sommes à {papier_mm} mm")