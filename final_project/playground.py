from application import Bouquet,PrettyBouquet, BouquetBox, Stock,PrettyStock, check_the_stock, \
    prepare_shopping_list, shopping_list_archive

print('--------------------------')
print('Customer facing showcase')
print('--------------------------')
print('')

# create the flowers dict for multiple bouquets, containing flowers and quantities

Christmas_Spirit_Bouquet_flowers = {
'White Roses':3
'White Bloom Chrysanthemums':5
'White Tipped Pine Cones':3
'Laurel':5
}

Christmas_Spirit_Bouquet = Bouquet(
    "Christmas Spirit Bouquet",
    Christmas_Spirit_Bouquet_flowers
)


Smiles&Sunshine_Bouquet_flowers = {
    'Peruvian Lily: 7,
    'rose':9 
    }

Smiles&Sunshine_Bouquet = Bouquet(
    "Smiles & Sunshine Bouquet",
    Smiles&Sunshine_Bouquet_flowers
)


Christmas_Celebration_Bouquet_flowers = {
    'Red Amaryllis':1
    'Red Hypericum':1
    'Purple Bloom Chrysanthemums':2
    'Red Gerbera':2
    'Purple Germini':3
    'Red Spray Roses':2
    'Burgundy Carnations':3
    'Rai Cones':2
    'Rhodo':2
    'Conifer':3
}

Christmas_Celebration_Bouquet = Bouquet(
    "Christmas Celebration Bouquet",
    Christmas_Celebration_Bouquet_flowers
)

White_Medley_Bouquet_flowers= {
    'White Spray Stocks':3
    'White Rose':5
    'White Double Lisianthus':5
    'White Trachelium':5
    'Eucalyptus':3
}

White_Medley_Bouquet_flowers = Bouquet(
    "White Medley Bouquet",
    White_Medley_Bouquet_flowers
)

Rainbow_Alstroemeria_Bouquet_flowers = {
    'White Alstroemeria':3
    'Pink Alstroemeria':3
    'Yellow Alstroemeria':3
    'Red Alstroemeria':3
    'Orange Alstroemeria':2
    'Cerise Alstroemeria':2
}


Rainbow_Alstroemeria_Bouque_flowers = Bouquet(
    "Rainbow Alstroemeria Bouque",
    Rainbow_Alstroemeria_Bouque_flowers
)


# create instances for each bouquet by its title and dict of ingredients
print('\n\033[34m BOUQUETS \033[0m\n')

Christmas_Spirit_Bouquet = PrettyBouquet("Christmas Spirit Bouquet", Christmas_Spirit_Bouquet_flowers)
print(Christmas_Spirit_Bouquet)
# print(Christmas_Spirit_Bouquet.__repr__())