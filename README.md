

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
[grab-images-from-page.py](grab-images-from-page.py)



---

why not saving some bing search
```
pip install bing-image-downloader
```
and 
```
from bing_image_downloader import downloader
query_string='axel springer verlag news pictures'
downloader.download(query_string, limit=100, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
```
## 8.  converting outlook pst files to MBOX format

there are plent y of converters of course paid software which is obvious though <b>
 once you want to spend some 5 minutes more and install one more library on your ubuntu or other linux machine
 everything could be done eqally good.
 I am saying here about pst-utils:
 
 ```
 sudo apt install pst-utils
 ```
 Then you need to find where on your outlook subdirectories pst files are stored or just export them from the menu
 and convert with:
 
 ```
readpst -ur Outlook.pst
 ```
 there are extra options like output directory etc according to your needs . 
 After couple of minutes ~1GB depends on the size you have directories with subdirectories and MBOX files ready to use <b>
 Those could be imported to MBOX based mail clients.
 
 ## G.  Gradio

<p>After a bit more than two years GPT3 is alife and kicking </p>if you want to play with openAI API used for the Chatboot with the help of gradio package</p> below is the

[notebook](GPT-3-gradio-RevA.ipynb)

All this is sugessted by OpenAI itself

---

<style>
    .container {
        width: 800px;
        text-align: justify;
    }
</style>

<div class="container">

Gradio can be used to create a user interface for OpenChat, which is an open-source chatbot framework. To connect Gradio to OpenChat, you can follow these general steps:
* First, create a chatbot using OpenChat, following the documentation and tutorials available on its official website or GitHub repository.

* Once you have a functional chatbot, you can use Gradio to create a user interface for it. Gradio allows you to create simple web-based UIs for your machine learning models, including chatbots.

* To create a Gradio interface for your chatbot, you can define a Python function that takes user input as an argument and returns the chatbot response. This function should use the OpenChat API to process the user input and generate the chatbot response.

* Once you have defined the function, you can use Gradio's Interface class to create a UI for it. You can define the UI components, such as text input fields and buttons, and connect them to your chatbot function.

* Finally, you can launch the Gradio interface using the launch method, which will start a web server and open the UI in your web browser.


</div>

Here is some sample code that demonstrates how to connect Gradio to OpenChat:

```

import openchat
import gradio as gr

# Create an OpenChat chatbot
chatbot = openchat.Chatbot()

# Define a function that takes user input and returns the chatbot response
def chatbot_response(text):
    response = chatbot.get_response(text)
    return str(response)

# Define the Gradio interface components
inputs = gr.inputs.Textbox(label="Enter text")
outputs = gr.outputs.Textbox(label="Chatbot response")

# Define the Gradio interface
interface = gr.Interface(chatbot_response, inputs, outputs, title="OpenChat Bot")

# Launch the Gradio interface
interface.launch()

```


<style>
    .container {
        width: 800px;
        text-align: justify;
    }
</style>


<div class="container">
    <p>This code defines a chatbot_response function that takes user input as an argument, uses the OpenChat API to process the input, and returns the chatbot response. It then defines a Gradio interface that includes a text input field and a text output field, which are connected to the chatbot_response function. Finally, it launches the Gradio interface</p>
</div>



---



## Technologies

_Created by:_ [lencz.sla@gmail.com]

