import os
from os import path
from os.path import dirname, realpath,join
import PyQt5
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets,QtCore,QtGui,uic,QtPrintSupport
from PyQt5.QtWidgets import *   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import numpy as np
import pandas as pd
from pydub import AudioSegment
import imagehash
from imagehash import hex_to_hash
from PIL import Image
import librosa as lib
from scipy import signal
from similarityfile import *

import logging 
logging.basicConfig(filename="logging_main.py.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 

logger=logging.getLogger() 
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

scriptDir=dirname(realpath(__file__))
From_Main,_= loadUiType(join(dirname(__file__),"MAIN.ui"))

class MainApp(QtWidgets.QMainWindow,From_Main):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        music= pd.read_excel('/home/fatma/dsp_task4/songsDataBase6.xlsx')
        self.songnames=music["song"].tolist()
        self.DataBase_songs = music[:].values  
        logger.info("init")
        logger.info("songs data base has been saved and it has "+str(len(self.DataBase_songs))+" songs in it")
        self.definefunctions()
        
        # variables 
        self.mixersongs=[None,None]
        self.songs_frate=[None,None]
        self.MIX_RATIO.hide()
        self.RATIO.hide()
        self.resultsTable.hide()
           
    def definefunctions(self):
        self.actionLoad_song.triggered.connect(lambda:self.compare_1song())
        self.SONG1.clicked.connect(lambda:self.compare_2songs(0))
        self.SONG2.clicked.connect(lambda:self.compare_2songs(1))
        self.MIX_RATIO.sliderReleased.connect(lambda:self.get_mixer_similarity())
        
    def read(self):
        load_file = QtWidgets.QFileDialog.getOpenFileName(None, "Load Audio File %s",filter="*.mp3")
        path=load_file[0]
        audiofile = AudioSegment.from_mp3(path)[:60000] 
        data = np.array(audiofile.get_array_of_samples())
        rate = audiofile.frame_rate
        # print(self.data)
        logger.info("the song in uploaded with data")
        logger.info(str(data))
        # print("data=",data,"rate",rate)
        return data,rate
    
    def compare_1song(self):
        logger.info("comparing 1 song with the database")
        data,rate=self.read()
        hashes_list =self.get_hashes_list(data,rate)    
        similarityindex=self.get_similarity_indexes(hashes_list)

    def mixer(self):
        logger.info("mixing 2 songs' data")
        self.slidervalue=self.MIX_RATIO.value() / 100.0
        if (len(self.mixersongs[0])<= len(self.mixersongs[1])):
            self.new_data=self.mixersongs[0]*self.slidervalue+(1-self.slidervalue)*self.mixersongs[1][:len(self.mixersongs[0])]
            return self.new_data,self.songs_frate[0]
        else:
            self.new_data=self.mixersongs[0][:len(self.mixersongs[1])]*self.slidervalue+(1-self.slidervalue)*self.mixersongs[1]
            return self.new_data,self.songs_frate[1]
    
    def compare_2songs(self,id):
        logger.info("adding song of id "+str(id)+"to the compare function")
        self.mixersongs[id],self.songs_frate[id]=self.read()
       
        if(id==1):
            self.MIX_RATIO.setValue(0)
            self.MIX_RATIO.show()
            self.RATIO.show()
            logger.info("2 songs were added to the mixer")
            self.get_mixer_similarity()
        else: print("there is 1 song only ")
           
    def get_mixer_similarity(self):
        data,rate=self.mixer()
        logger.info("extracting the similarity indexes")
        hashes=self.get_hashes_list(data,rate)
        similarity=self.get_similarity_indexes(hashes)
        self.get_table(similarity)
        print("similarity indexes ",self.all_similarity_index)
                  
    def get_hashes_list(self,data,rate):
            self.hashes=[]
            sampleFreqs,sampleTime, colorMesh = signal.spectrogram(data,fs=rate)
            spect_hash=self.get_hash(colorMesh)
            self.hashes.append(spect_hash)
            for feature in self.get_features(data,colorMesh,rate):
                self.hashes.append(self.get_hash(feature))
            logger.info("the song hashes=")
            logger.info(self.hashes)
            return self.hashes
    
    def get_hash(self,array):
        dataInstance = Image.fromarray(array)
        PHASH= imagehash.phash(dataInstance, hash_size=16).__str__()
        return PHASH

    def get_features(self,data,color,rate):
        features_list=[lib.feature.mfcc(y=data.astype('float64'),sr=rate),
               lib.feature.melspectrogram(y=data,sr=rate,S=color),
               lib.feature.chroma_stft(y=data,sr=rate,S=color)]
        return features_list

    def get_similarity_indexes(self,hashes):
        logger.info("get similarity index")
        self.all_similarity_index = similarity_indexes(self.DataBase_songs,hashes)
        return self.all_similarity_index
        
    def get_table(self,similarity_list):
        # self.resultsTable.show()
        self.resultsTable.setColumnCount(2)
        self.resultsTable.setRowCount(len(similarity_list))
        for row in range(len(similarity_list)):
            self.resultsTable.setItem(row, 1, QtWidgets.QTableWidgetItem( self.songnames[row] )  )
            self.resultsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(round(similarity_list[row], 2))+"%"))
     
            self.resultsTable.verticalHeader().setSectionResizeMode(row, QtWidgets.QHeaderView.Stretch)

        self.resultsTable.setHorizontalHeaderLabels([ "similarity percentage","song names"])
        self.resultsTable.show()


    
      

app = QtWidgets.QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec_())

