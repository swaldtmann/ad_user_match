# ad_user_match

A Python script to 


## Create Environment

    pipenv install
    pipenv shell

## create .env file

    vi .env

Add the following with the correct data for your purpose

    # .env 
    AD_DUMP_FILE_1=<your file with path here>
    AD_DUMP_FILE_2=<your file with path here>
    OUT_FILE=<your file with path here>

    #
    # End of .env

## Run the script with

    pipenv run ad_user_match.py
