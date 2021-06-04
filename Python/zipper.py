import time
import os
import sys
import zipfile

startTime = time.time()
# Function to compress a directory
def zip_directory(path_zip, filename):

    zipf = zipfile.ZipFile( filename, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path_zip):
        for file in files:
            zipf.write(os.path.join(root, file))

    zipf.close()
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))

# Function to unzip a zip file
def unzip_directory( path_unzip, filename):

    with zipfile.ZipFile( filename, 'r') as zip_ref:
       zip_ref.extractall( path_unzip)
       executionTime = (time.time() - startTime)
       print('Execution time in seconds: ' + str(executionTime))

# Fucntion to show the content of a Zip file
def zip_view( filename):

     with zipfile.ZipFile( filename) as file:
        file.printdir()


# Help for using the script
def help():
    print(""" Wrong parameter:

    Usage:
        python zip-directory.py Zip path filename       # To zip directory recursively
        python zip-directory.py UnZip path filename     # To un Zip
        python zip-directory.py View filename           # To view files in zip archive
    """)


# Initialize program
#
if __name__ == '__main__':

    # check if they pass any parameter, if there is no parameter it jumps to the error message
    #
    if len(sys.argv) > 1:

        # If the first parameter is the word "Zip" => Compress
        #
        if ( sys.argv[1] == 'Zip'):

            # review the following two parameters that have been entered to obtain
            # the path to zip and the name that we will give to the zip file
            #
            # Here you would have to place the validation so that in case these two
            # parameters did not come will generate an alert or error
            #
            filename =  sys.argv[3]
            path =  sys.argv[2]

            # We write on the screen what the script is going to do
            print( sys.argv[1] + ": directory: " + path + " into file: " + filename)

            # Llamamos a la funcion que zipea
            zip_directory( path, filename)

         # If the first parameter is the word "UnZip" => Unzip
         #
        elif( sys.argv[1] == 'UnZip'):

            # We review the following two parameters that have been entered to obtain
            # the path where we will unzip and the file to unzip
            #
            # Here you would have to place the validation so that in case these two
            # parameters did not come will generate an alert or error
            #
            filename =  sys.argv[3]
            path =  sys.argv[2]

            # We write on the screen what the script is going to do
            print( sys.argv[1] + ": file: " + filename + " directory: " + path)

            # LLamamos a la función para descomprimir
            unzip_directory( path, filename)

        # If the first parameter is the word "View" => See content of the zip file
         #
        elif( sys.argv[1] == 'View'):

            # It only requires one more parameter which is the name of the zip file
            #
            # Here you would have to place the validation so that in case these two
            # parameters did not come will generate an alert or error
            #
            filename =  sys.argv[2]

            # We write on the screen what the script is going to do
            print( sys.argv[1] + ": file: " + filename )

            # We call the function to display the file
            zip_view( filename)

        else:
            # We call the show help function
            #
            print( sys.argv[1] + ": unknown command")
            help()

    else:
        # We call the show help function
        #
        print( "Unknown command")
        help()


    sys.exit()
  #print exection time
