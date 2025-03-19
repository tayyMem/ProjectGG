run the anaconda prompt as admin
go to your environment
install below libraries

pip install streamlit
pip install transformer torch

there might be some libraries you will have to install based on what you have and do not have.

To run the model, there are 2 options.

OPTION1
download test2.py file to your environment's path and run test2.py file directly. But then, there will be no heading as some adjustments were done to heading with sidebar configuaration. 
streamlit run test2.py 


OPTION2
download all files under collection (except readme.md) to your anaconda environment path. and there shall be .streamlit folder in your environment. download the 2 files under my .streamlit folder and put it in your .streamlit folder. then run below. 
streamlit run page1.py
