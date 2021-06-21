# wget -r -k -l 7 -p -E -nc https://mypizza.kg/
import os 

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'breakfast')
os.remove(path)