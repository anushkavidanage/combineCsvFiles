"""
Created in August 2018
by Anushka Vidanage

"""

# Example call:
# python combine_csv.py /home/users/Anushka/Desktop final_combined_file.csv

# Import libraries
import glob
import pandas

def concat_csv(input_dir, output_file, header_line=True):
  
  """
  Combine a set of cvs files into one csv file. If header_line 
  is set to True the programme will remove the headers from
  all files and the result file will only contain one header line
  
  Inputs:
    - input_dir:    Path to directory containing all csv files
    - output_file:  Name of the output csv file
  """
  
  header_list = [] # A list for storing header labels
  df_list = [] # A list for storing dataframes of csvs
  
  # Get all .csv files from the defined directory
  csv_file_list = glob.glob(input_dir+'*.csv')
  
  file_num = 0
  
  # Loop over each csv file and generate dataframes
  # from those files
  #
  for file_name in csv_file_list:
    file_num += 1
    
    print ' Reading file number:', file_num
    print ' File name:', file_name
    print
    
    if(file_num == 1):
      df = pandas.read_csv(file_name)
      header_list = list(df.columns)
    
    df = pandas.read_csv(file_name, header=None)
    
    if(header_line):
      df.drop([0], inplace=True)
      
    df_list.append(df)
  
  print '### Concatenating csv files into one csv'
  print
  
  # Concatenate dataframes together
  concat_df = pandas.concat(df_list, axis=0)
  
  # Assign the header list
  concat_df.columns = header_list
  
  # Write to csv
  concat_df.to_csv(output_file, index=None)
  
  print '### Output csv file %s created' %output_file
  print

#===============================================================================
# Main programme
#===============================================================================

csv_dir_path =    sys.argv[1] # Path to the directory where all the csv files are
output_file_name = sys.argv[2] # Output csv file name

# Check whether output filename has the .csv extension
#
if('.csv' not in output_csv_name):
  output_file_name += '.csv'

# Calling the concatenation csv function
#
concat_csv(csv_dir_path, output_file_name)

  
  
  
