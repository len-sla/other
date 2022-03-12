

## 1.  [ase-visualization-of-molecules.ipynb](ase-visualization-of-molecules.ipynb)
---
Package ase is prepared for 3D Visualization of Molecules. Package to do that is available on gitlab: [ase ](https://gitlab.com/ase/ase).

* Library needs two tables one is where atoms have their coordinates x,y,z and another coresponding with keys=symbols.
* It could be just four columns in table csv, or pandas with columns x,y,x, symbol.

![Mole ](mole.PNG)
 



---
## 2.  [Keras-neural-net-for-champs.ipynb ](Keras-neural-net-for-champs.ipynb)


Task here is 
*  predicting the scalar_coupling_constant between atom pairs in molecules, given the two atom types (e.g., C and H),
 the coupling type (e.g., 2JHC), and any features you are able to create from the molecule structure (xyz) files


![Molecules ](rotating.gif)

---


## 3.  [wiki_download.ipynb ](wiki_download.ipynb)


For diifferent NLP or GPT models and task input is the data.
One of the sources of the data is wikipedia. Based on collected and processed data from wikipedia at the end there is a txt file,
in  this particualr case plwiki is being collected to be able further train non english tokenizer and GPT 2 model

---
## 4.  [max_size_occup.py ](max_size_occup.py)

* Automatically  delete oldest files from given folder and keep used capacity within given limit
on the   Raspberry Pi.  
I've  tried to find as simple as possible  functions and use them.
   
It looks like os and glob libraries are doing their job and are able to handle easiest way everything.   
   
There are only two simple functions:
>* _sorted_dir_list()_    which is creating sorted list with given folder as input
>* _to_big_delete_oldest(40)_   function which  delete oldest files up to given limit( capacity in GB) with given granularity here 100 files  

executing is simple:   $ _python max_size_occup.py_


  
  Of course the libraries pathlib and glob should be installed before if necessary. To be able to do it automatically there is need  to do  execution through 
[CRONTAB](https://linuxhandbook.com/crontab/) so cleanup will be done periodically as defined by user 
#

## 5.  [olx-table.ipynb ](olx-table.ipynb)


Task here was 
*   to scrap the webpage  where main structure was based on the table structure.
Information after cleaning with some simple REGEX was saved  as pandas databse for later comparison and use.

## 6.  [data science  with docker](aa.jpg)
To extend cpabilities of docker container is sometimes required update some internal packages or install something neww.
That was the case this time. There was need to add ffmpeg inside as getting information about the media files through ffprobe 
was not easy.
First it is good to know what type of os is inside docker container:


```
cat /etc/os-release
```

and it gives answer like :

```
NAME="Ubuntu"
VERSION="20.04 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```



then checking what kind of pip packages are installed

```
pip list 
```
do standart update
```
apt-get update 
```
and 

```
apt install ffmpeg
```
## 6.  Scrap couple of mp3 from the webpage for the ML JINA purpose

To test some multimodal capabilities of JINA framework there was need to find example mp3 files in this case birds voices.
To scrap free of charge sounds of birds urllib request, BeautifulSoup library was used and the piece of code like below

```
import requests
import urllib.request
import re
from bs4 import BeautifulSoup

r = requests.get('https://quicksounds.com/library/sounds/animal')
soup = BeautifulSoup(r.content, 'html.parser')

for a in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
    filename = a['href'][a['href'].rfind("/")+1:]
    doc = requests.get(a['href'])
    with open(filename, 'wb') as f:
        f.write(doc.content)

```
## 7.  Scrap couple of pictures from the webpage for the ML JINA purpose

first if its static webpage:
```
from bs4 import *
import requests
import os

# CREATE FOLDER
def folder_create(images):
	try:
		folder_name = input("Enter Folder Name:- ")
		# folder creation
		os.mkdir(folder_name)

	# if folder exists with that name, ask another name
	except:
		print("Folder Exist with that name!")
		folder_create()

	# image downloading start
	download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):

	# initial count is zero
	count = 0

	# print total images found in URL
	print(f"Total {len(images)} Image Found!")

	# checking if images is not zero
	if len(images) != 0:
		for i, image in enumerate(images):
			# From image tag ,Fetch image Source URL

						# 1.data-srcset
						# 2.data-src
						# 3.data-fallback-src
						# 4.src

			# Here we will use exception handling

			# first we will search for "data-srcset" in img tag
			try:
				# In image tag ,searching for "data-srcset"
				image_link = image["data-srcset"]
				
			# then we will search for "data-src" in img
			# tag and so on..
			except:
				try:
					# In image tag ,searching for "data-src"
					image_link = image["data-src"]
				except:
					try:
						# In image tag ,searching for "data-fallback-src"
						image_link = image["data-fallback-src"]
					except:
						try:
							# In image tag ,searching for "src"
							image_link = image["src"]

						# if no Source URL found
						except:
							pass

			# After getting Image Source URL
			# We will try to get the content of image
			try:
				r = requests.get(image_link).content
				try:

					# possibility of decode
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					# After checking above condition, Image Download start
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					# counting number of image downloaded
					count += 1
			except:
				pass

		# There might be possible, that all
		# images not download
		# if all images download
		if count == len(images):
			print("All Images Downloaded!")
			
		# if all images not download
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

# MAIN FUNCTION START
def main(url):

	# content of URL
	r = requests.get(url)

	# Parse HTML Code
	soup = BeautifulSoup(r.text, 'html.parser')

	# find all images in URL
	images = soup.findAll('img')

	# Call folder create function
	folder_create(images)


# take url
url = input("Enter URL:- ")

# CALL MAIN FUNCTION
main(url)
```

---

why not saving some bing search

## Technologies

_Created by:_ [lencz.sla@gmail.com]

