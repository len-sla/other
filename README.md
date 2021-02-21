

## 1.  [ase-visualization-of-molecules.ipynb](ase-visualization-of-molecules.ipynb)
---
Package ase is prepared for 3D Visualization of Molecules. Package to do that is available on gitlab: ase.

* Library needs two tables one is where atoms have their coordinates x,y,z and another coresponding with keys=symbols.
* It could be just four columns in table csv, or pandas with columns x,y,x, symbol.

![Mole ](mole.PNG)
 



---
## 2.  [max_size_occup.py ](max_size_occup.py)

* Automatically  delete oldest files from given folder and keep used capacity within given limit

### General info
Keep tidy( delete oldest files) USB memory stick on the  on the Raspberry Pi.  
I've  tried to find as simple as possible  functions and use them.
   
It looks like os and glob libraries are doing their job and are able to handle easiest way everything.   
   
There are only two simple functions:
>* _sorted_dir_list()_    which is creating sorted list with given folder as input
>* _to_big_delete_oldest(40)_   function which  delete oldest files up to given limit( capacity in GB) with given granularity here 100 files  

executing is simple:   $ _python max_size_occup.py_


  
  Of course the libraries pathlib and glob should be installed before if necessary. To be able to do it automatically there is need  to do  execution through 
[CRONTAB](https://linuxhandbook.com/crontab/) so cleanup will be done periodically as defined by user 
### Technologies

_Created by:_ [@len-sla]

