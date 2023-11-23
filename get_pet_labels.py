#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Shaik Masroor Ahmed 
# DATE CREATED: 08-12-2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Making the list of all the image lables using the listdir function for os 
    filename_list = listdir(image_dir)
    
    # Creating an empty dictionary named results_dic
    results_dic = dict()
    
    # Lower casing the pet labels and removing the numeric content from the label for appending in the pet_labels list.
    
    
    for idx in range(len(filename_list)):
        
        if filename_list[idx][0] != ".":
            
            low_pet_image = filename_list[idx].lower() #sets pet label name to lower case letters
            
            word_list_pet_image = low_pet_image.split("_") #splits the lower case string to words separated by _
            
            pet_name = ' '.join([word for word in word_list_pet_image if word.isalpha()])# loops to check only the pet_name contains only alphabets and if yes then adds to pet name with the white spaces.
            
            pet_name = pet_name.strip() #strip off starting or trailing whitespace if                                        any.
            
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_name]
            else:
                print("**warning: Key= ", filename_list[idx], "already exists in results_dic with value= ", results_dic[filename_list[idx]])
        
    return results_dic
