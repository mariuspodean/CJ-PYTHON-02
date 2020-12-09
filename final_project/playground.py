from application import Bouquet, PrettyBouquet, BouquetBox, enter_store

# create the flowers dict for multiple bouquets, containing flowers and quantities

Christmas_Spirit_Bouquet_flowers = {
    'White Roses':3,
    'White Bloom Chrysanthemums':5,
    'White Tipped Pine Cones':3,
    'Laurel':5,
}

Christmas_Spirit_Bouquet = Bouquet(
    "Christmas Spirit Bouquet",
    Christmas_Spirit_Bouquet_flowers
)


Smiles_Sunshine_Bouquet_flowers = {
    'Peruvian Lily': 7 ,
    'Rose':9 
    }

Smiles_Sunshine_Bouquet = Bouquet(
    "Smiles & Sunshine Bouquet",
    Smiles_Sunshine_Bouquet_flowers
)


Christmas_Celebration_Bouquet_flowers = {
    'Red Amaryllis':1,
    'Red Hypericum':1,
    'Purple Bloom Chrysanthemums':2,
    'Red Gerbera':2,
    'Purple Germini':3,
    'Red Spray Roses':2,
    'Burgundy Carnations':3,
    'Rai Cones':2,
    'Rhodo':2,
    'Conifer':3
}

Christmas_Celebration_Bouquet = Bouquet(
    "Christmas Celebration Bouquet",
    Christmas_Celebration_Bouquet_flowers
)

White_Medley_Bouquet_flowers= {
    'White Spray Stocks':3,
    'White Rose':5,
    'White Double Lisianthus':5,
    'White Trachelium':5,
    'Eucalyptus':3
}

White_Medley_Bouquet = Bouquet(
    "White Medley Bouquet",
    White_Medley_Bouquet_flowers
)

Rainbow_Alstroemeria_Bouquet_flowers = {
    'White Alstroemeria':3,
    'Pink Alstroemeria':3,
    'Yellow Alstroemeria':3,
    'Red Alstroemeria':3,
    'Orange Alstroemeria':2,
    'Cerise Alstroemeria':2
}

Rainbow_Alstroemeria_Bouquet = Bouquet(
    "Rainbow Alstroemeria_Bouquet",
    Rainbow_Alstroemeria_Bouquet_flowers
)
Christmas_Spirit_Bouquet = PrettyBouquet("Christmas Spirit Bouquet", Christmas_Spirit_Bouquet_flowers)

stock=[
    Christmas_Spirit_Bouquet,
    Smiles_Sunshine_Bouquet,
    Christmas_Celebration_Bouquet,
    White_Medley_Bouquet,
    Rainbow_Alstroemeria_Bouquet
]

bouquet_box = BouquetBox(stock)

for item in enter_store(bouquet_box):
    print(str(item))
