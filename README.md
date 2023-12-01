# Analysis of Pokemon Mono-types and Dual-types Generations

## Overview
A Pokemon can have one or two types. A mono-type is a pokemon with only one type, while a dual-type is a pokemon with two types. This project explores the variance of mono vs dual types in each pokemon generation to answer the question:
- Which generation is predominately composed of monotypes vs dualtypes?

It accomplishes this by pulling generational and species datasets from PokeApi. Along the way, it was discovered that some of PokeApi's endpoint routes were broken, so the broken ones were recorded down into a "broken_endpoints.json", which could be helpful for the PokeApi maintainers.

## Set-up Instructions
Please make sure you have VSCode, Python3, Jupyter Notebook installed on your computer.
- Clone the repo to a local folder on your computer.
- In the root project directory, create a virtual environment by running the command `python3 -m venv venv`
- Next activate the virtual environment by running:
  - `venv\Scripts\Activate.ps1` for Windows
  - `venv/bin/activate` for Unix/macOS
- Then install the project dependencies by running `pip install -r requirements.txt`
- Open up the project in VSCode, and open "pokemon_analysis.ipynb".
- Click "Run all" to run all cells
<div align="center">
  <img width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/080f0063-4f6d-4754-9a57-75916b89468b">  
</div>

### Disclaimer: 
In the Data Fetching portion of this project, we will fetch data for every single pokemon there is, which means there will be over a thousand api calls and might take over 5-10 minutes depending on your network connection
<div align="center">
  <img width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/36c3b679-9976-48d8-a9bf-db09f77710dc">
</div>

- If you need to skip the Data Fetching part due to connectivity issues, jump to Data Clean-Up section and run from there. (If you restarted the kernel and jumped Data Clean-up, make sure to rerun cell 1 to get all the imports statements)
    - Future improvements of this project will utilize the `data/Generation_X` jsons as an offline data fetching alternative 

<div align="center">
  
</div>


## Features
- Read TWO data sets in with an API (or use two different APIs that have data you can combine to answer new questions)
  - pulled api datasets for generations and individual species (many, many api requests to gather all the necessary data)
<div align="center">
  <img width="600" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/4b9567a2-3ab9-4e48-ac99-e7bfd197d195">
</div>
<div align="center">
  <img width="600" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/35392ed3-f254-4bd7-9b92-798c82839b02">
</div>
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.
<div align="center">
  <img width="600" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/dafc6051-8159-48f0-ae46-992a59fdbcbe">
</div>
<div align="center">
  <img width="600" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/b0c6885f-8b33-4c65-ab7b-9b424e64fb4e">
</div align="center">
- Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.
<p align="center">
  <img height="400" width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/37b99b07-65ab-48f0-a529-c7b405494240">
  <img height="400" width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/ec35d455-4928-4a43-a91b-6969e4937c67">
  <img height="400" width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/3a9f73ac-19d8-4cb3-805c-b42a09527eef">
  <img height="400" width="400" alt="image" src="https://github.com/kevinle108/data-analysis-2023/assets/54592360/5381efe2-8f67-473d-af6a-5ca881bcd66d">  
</p>
- Utilize a virtual environment and include instructions in your README on how the user should set one up
  - See Set-up Instructions section     
- Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. Tidy up your notebook, and make sure you don’t have any empty cells or incomplete cells that don’t do anything. Make sure it’s all functional before your final github commit.
  - See comments throughout the "pokemon_analysis.ipynb" notebook.

## Special Thanks
- Thank you to Tre, Von, and the entire Code:You organization for providing a wonderful community to learn Python and Data Analysis!
- Thank you to PokeApi for providing such an extensive and free api - Learn more about it here: https://pokeapi.co/ 
