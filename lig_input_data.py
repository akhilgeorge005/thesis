

from sklearn.ensemble import RandomForestRegressor

def input_data():
    
    # DEFINE CUSTOM MODEL TO INSERT INTO MODEL SELECTION LIST
    
    #########################################################
    
    # rfr = RandomForestRegressor(n_estimators = 750, verbose = 2)
    
    #########################################################
    
    #### GENERIC INFO ###
    # the input df is better having a columns 'year' (year of fire) and 'season' (value 1 winter and 2 summer)
    # coordinates must be called as x and y
    # in input dfa column name natural_reg can be added with more info about the vegetated zones
    # points and fire df must be .pkl format
    # I want a column 'point_index' in points_df
    # are you going to do a regression? fires_df has to have a column called 'fire' for describing their frequency
    # put 1 fold if you want to skip the validation
    
    input_data = {'region_name'       : 'LiguriaNew',
                  'path_dem'          : '/home/gruppo4/Regioni/Liguria/new_data_32632/dem_100_32632.tif',          # path of the dem tif file
                  'ntree'             : 1000,
                  # if True the test dataset is created by taking random points
                  'random_years'      : False, 
                  # starting year of wildfire dataset                                      
                  'year_from'         : 2007, 
                  # the year in which the test dataset is created if random_years = False, otherwise it takes random points among year = last year - year_test                                     
                  'year_test'         : 2015,  
                  # the last year of the time period considered for the wildfires                                    
                  'year_to'           : 2019,    
                  # put the output path with the / final. Note that inside there will be ceated a new output folder with the experiments
                  'data_dir'          : '/home/gruppo4/Regioni/Liguria/new_data_32632/',
                  # True if i use 2 different datasets for training and for creating the final map
                  'two_points_df'     : False, 
                  # path of the training dataset                                    
                  'training_df_path'  : '/home/gruppo4/Regioni/Liguria/new_data_32632/points.pkl',#, '/home/gruppo4/liguria-fire-susceptibility/data_lig_s/points_clc.pkl'
                  # path of the dataset for the final susceptibility map
                  'all_points_path'   : '/home/gruppo4/Regioni/Liguria/new_data_32632/points.pkl', #'/home/gruppo4/liguria-fire-susceptibility/data_lig_s/points_clc.pkl', 
                  # path fires dataset: make sure to ahve a year column called 'year'
                  'fires_df_path'     : '/home/gruppo4/Regioni/Liguria/new_data_32632/fires.pkl', #'/home/gruppo4/liguria-fire-susceptibility/data_lig_s/fires_clc.pkl',                     
                  ############### MODEL DATA ####################
                  # columns to be excluded: give a look at the next parameter for excluding the perc columns
                  'excluded_col'      : ["point_index",'x', 'y', "row", "col",
                                         "veg_freq",
                                         'geometry'], 
                  # if it is True perc columns will be excluded, if you want to use these and not the is_veg_ cols check the next parameter                             
                  'exclude_perc'      : True,  
                  # this exclude the is_veg columns produced by one hot encoding, select True if perc columns are used instead of these                                        
                  'exclude_is_veg'    : False, 
                  # list of the number of folds per experiment                                    
                  'n_fold'            : [1], 
                  # if it is true there wont be any model selection but the only algorithm used is a random forest with nestimators = ntree                                      
                  'random_forest'     : True, 
                  # if False you will perform regression                                     
                  'classification'    : True, 
                  # insert a model defined in the first section of this file, put None if random_forest = True
                  'model_selection'   : [None], 
                  # give a list of names of the model selected previously
                  'name_sel_models'   : [],
                  # use tplot for searcing the optimal algorithm --> give random_forest = True for switching to this option and put n_fold = [1]
                  'tpot_sel'          : False,
                  # select which season is considered, 1 is winter and 2 is summer                                       
                  'season'            : [1,2],  
                  # give a name that describe the experiment: it is related to the excluded columns                                    
                  'type'              : 'dem100_1000t_2007-15',  
                  # number of cells for doing the k fold validation in the x direction, then in the y                           
                  'tiles_x'           : 70, #7,                                         
                  'tiles_y'           : 50, #5,
                  # if it is True the prediction on points_df is an avarage of the different predictions on the fold used in the validation phase
                  'predict_points_on_fold' : False,
                  # define the quantiles for the burned area analisys 
                  'quantile'          : [0.25, 0.5, 0.75, 0.9, 0.95],
                  # insert the fires shapefile with the column year for quantile burned area analysis (put None if you dont have it)
                  'path_fires_shp'    : '/home/gruppo4/Regioni/Liguria/new_data_32632/fires_y_32632.shp',
                  # insert the fires raster file for the same analysis of before in case you dont have a shp file (put None before)
                  'path_fires_raster' : None
                  
                  
        }
    return input_data
    


