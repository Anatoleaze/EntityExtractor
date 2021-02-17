# -*- coding: utf-8 -*-

import spacy 
from spacy import displacy  
from bs4 import BeautifulSoup
import requests

class Work:
    def __init__(self):
        self.nlp=spacy.load("fr_core_news_md")
        self.txt=""
        
    def getContentURL(self,url):
        page = requests.get(url)
        html = BeautifulSoup(page.content, 'html.parser')
        liste=html.find_all('p')
        for elt in liste:
            for child in elt.children:
                if 'getText' in dir(child):
                    self.txt+=child.getText()+" "
        return self.txt
    
    def getContentFile(self,filename):
        f=open(filename)
        for ligne in f:
            self.txt+=ligne.strip()
        f.close()
        return self.txt
    
    def getContentFreeTxt(self,txt):
        self.txt=txt
        return self.txt
    
    def getTxt(self):
        return self.txt
    
    def analyseText(self):
        doc=self.nlp(self.getTxt())
        colors = {"PER":"#1d8523","LOC":"#7aecec","ORG":"#ff9561","MISC":"#ff33d1"}
        return displacy.render(doc, style="ent",options={"colors": colors},jupyter=False)
    
    def getTypesEntity(self,html):
        res={}
        code= BeautifulSoup(html, 'html.parser')
        liste=code.find_all("mark")
        for elt in liste:
            cat=elt.find("span").getText()
            entity=elt.getText().replace(cat,"")
            if cat not in res.keys():
                res[cat]=[entity]
            else:
                if entity not in res[cat]:
                    res[cat].append(entity)
        return res