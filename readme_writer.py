# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:21:02 2021

@author: shane
"""

from admin import fileverify, read_json, write_json, select_thing
import os
   
#TODO update this to reate a json file inside the repo with this information
#this will make future updates of readme much, much easier
#TODO modify this function to accept optional json argument for that reason

def dict_unpack(foldername):
    if fileverify(os.path.join(foldername,'readme_dict.json')):
        readme=read_json(os.path.join(foldername,'readme_dict.json'))    
        readme2=[]
        for k,v in readme.items():
            readme2.append(k)
            readme2.append(bre)
            readme2.append(v)
        readme=readme2[:]
        return(readme)
    else:
        return(None)

def readme_writer(foldername,purpose=None,backstory=None,prework=None,frequency=None,readme=None):
    #TODO make this tool more sophisticated to work with metaprogram 
    bre="\n"
    if readme:
        purpose=readme[2]
        backstory=readme[5]
        libs=readme[8]
        prework=readme[11]
        frequency=readme[14]

    if purpose:
        purpose=purpose
    else:
        purpose=input("In 1 brief sentence, please describe what this project does \n")
    if backstory:
        backstory=backstory
    else:
        backstory=input("In a few sentences, explain why it is/was needed\n")
    if 'requirements.txt' in os.listdir(foldername):
        libraries=os.path.join(foldername,'requirements.txt')
        with open (libraries,'r') as f:
            lines=f.readlines()
            libs=', '.join([line.split("=")[0] for line in lines])
    else:
        libs=""
    if prework:
        prework=prework
    else:
        prework=input('Is there anything a user needs to do prior to running? If yes, write that out below.\n')
    
    if frequency:
        frequency=frequency
    else:
        freq=['Continuously','Daily','Weekly','Monthly','As Needed']
        freqdict={str(ix):i for ix,i in enumerate(freq)}
        #TODO replace with stdout, add exception handling here
        print("How often is this intended to be run?")
        for ix,i in enumerate(freq):
            print(f'{ix}. {i}')
        frequency=freqdict[input('Please enter your selection number.\n')]
    #TODO include fancy formatting later
    readme1="## The purpose of this project is as follows:"
    readme2="## Here's some back story on why I needed to build this:"
    if len(libs)>1:
        readme3="## This project leverages the following libraries:"
    else: readme3="## This project uses only python built-in functions and data types."
    if len(prework)>2:
        readme4="## In order to use this, you'll first need do the following:"
        
    else:
        readme4="## This project does not require any special setup steps."
        prework=""
    readme5="## The expected frequency for running this code is as follows:"
    if readme:
        readme=readme
    else:
        readme=[readme1,bre,purpose,bre,readme2,bre,backstory,bre,readme3,
            bre,libs,bre,readme4,bre,prework,bre,readme5,bre,frequency]
    readme_file=os.path.join(foldername,"README.md")
    read_dict={a:b for a,b in zip(readme[::3],readme[2::3])}
    write_json(read_dict,os.path.join(foldername,'readme_dict'))
    with open(readme_file,'w') as f:
        f.writelines(readme)

def grab_readme(filename=None):
    if filename:
        filename=filename
    else:
        filename=os.path.join(os.getcwd(),'README.MD')
    with open(filename,'r') as f:
        x=f.read().split('\n')
        x.extend([None,None,None,None])
    return(x)

def rewrite_readme(foldername):
    os.chdir(foldername)
    jsonfile=dict_unpack(foldername)
    if jsonfile:
        readme_writer(foldername,readme=jsonfile)
    else:
        try:
            readlist=grab_readme()
        except:
            return(None)
        packlist=[]
        for i in range(4):
            packlist.append(select_thing([i for i in readlist if i not in packlist]))
        readme_writer(foldername,purpose=packlist[0],backstory=packlist[1],
                      prework=packlist[2],frequency=packlist[3])
            

def main(folder=None):
    if folder:
        folder=folder
    else:
        folder=os.getcwd()
    readme_writer(folder)

if __name__=="__main__":
    main()