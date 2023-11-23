from tabulate import tabulate
#As we have obtained the results now tabulating the obtained results for better comparision below
#We are tabulating the results with tabulate module from python packages.

#As we run sh run_models_batch.sh the Final_results.py will get executed and show us the table
number_list = [['Total Images','Dog Images','Not Dog Images'],
                   [40,30,10]]
print(tabulate(number_list, headers='firstrow',tablefmt='fancy_grid'))
    
stats = [['CNN Model Architecture', '% Not-a-Dog Correct', '% Dogs Correct', '%Match Label'],
         ['ResNet', '90.0%', '100.0%', '90.0%', '82.5%'],
         ['AlexNet', '100.0%', '100.0%', '80.0%', '75.0%'],
         ['VGG', '100.0%', '100.0%', '93.3%', '87.5%']]

print(tabulate(stats, headers = 'firstrow', tablefmt='fancy_grid'))
    