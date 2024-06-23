def create_categories(picks):



    picks['cigarette_waste'] = picks[['butts', 'lighters', 'cigaretteBox', 'tobaccoPouch',
                                                                 'skins', 'smoking_plastic', 'filters', 'filterbox',
                                                                 'vape_pen', 'vape_oil', 'smokingOther', 'degraded_lighters']].sum(axis=1)
    
    picks['food_packaging'] = picks[['FOOD','sweetWrappers',	'paperFoodPackaging',	'plasticFoodPackaging',
                                                              'plasticCutlery',	'crisp_small',	'crisp_large',	'styrofoam_plate',
                                                               'napkins',	'sauce_packet',	'glass_jar',	'glass_jar_lid',	'foodOther',
                                                                'pizza_box', 'aluminium_foil',	'COFFEE',	'coffeeCups',	'coffeeLids',	'coffeeOther',
                                                                'milk_bottle',	'milk_carton']].sum(axis=1)


    picks['general_packaging'] = picks[['spiritBottle', 'wineBottle', 'brokenGlass',	'bottleTops',
                                                                      'paperCardAlcoholPackaging',	'pint',	'plasticAlcoholPackaging',
                                                                       'six_pack_rings',    'alcohol_plastic_cups', 'alcoholOther', 'bottleLid',	'bottleLabel',
                                                                       'straws', 'plastic_cups',	'plastic_cup_tops', 'strawpacket',	'styro_cup',	'broken_glass',
                                                                       'condoms',	'nappies', 	'menstral', 'deodorant',	'ear_swabs',	'tooth_pick',	'tooth_brush',
                                                                       'sanitaryOther',	'gloves', 'degraded_plasticbottle',	'facemask',	'wetwipes',	'hand_sanitiser']].sum(axis=1)
                                                                     
    picks['deposit_waste'] = picks[['beerCan',	'beerBottle', 'waterBottle',	'fizzyDrinkBottle', 'tinCan',
                                                                   'sportsDrink', 'ice_tea_bottles',	'ice_tea_can',	'energy_can', 'softDrinkOther']].sum(axis=1)

    picks['chewing_gum_waste'] = picks[['chewing_gum']].sum(axis=1)    

    picks['other'] = picks[['microplastics',	'mediumplastics', 	'macroplastics',	'rope_small',	'rope_medium',	'rope_large',
                                              	'fishing_gear_nets',	'ghost_nets',	'buoys', 'degraded_plasticbag',	'degraded_straws',	'balloons',
                                                'lego',	'shotgun_cartridges', 	'coastal_other',	'styro_small',	'styro_medium', 	'styro_large']].sum(axis=1)
    
    return picks