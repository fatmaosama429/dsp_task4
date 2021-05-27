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
        self.DataBase_songs = music[:].values  
        print(len(self.DataBase_songs))
        logger.info("init")

        logger.info("songs data base has been saved and it has "+str(len(self.DataBase_songs))+" songs in it")
        print("songs data base has been saved and it has "+str(len(self.DataBase_songs))+" songs in it")
        self.definefunctions()
        
        # variables 
        self.hashes=[]
        
    def definefunctions(self):
        self.actionLoad_song.triggered.connect(lambda:self.compare_1song())

    def compare_1song(self):
        load_file = QtWidgets.QFileDialog.getOpenFileName(None, "Load Audio File %s",filter="*.mp3")
        path=load_file[0]
        audiofile = AudioSegment.from_mp3(path)[:60000] 
        self.data = np.array(audiofile.get_array_of_samples())
        self.rate = audiofile.frame_rate
        print(self.data)
        logger.info("the song in uploaded with data")
        logger.info(str(self.data))
        self.get_hashes_list()    
        self.get_similarity_indexes()
        
    def get_hashes_list(self):
            sampleFreqs,sampleTime, colorMesh = signal.spectrogram(self.data,fs=self.rate)
            self.spect_hash=self.get_hash(colorMesh)
            self.hashes.append(self.spect_hash)
            for fet in self.get_features(self.data,colorMesh,self.rate):
                self.hashes.append(self.get_hash(fet))
            logger.info("the song hashes=")
            logger.info(self.hashes)
            print(self.hashes)
    
    def get_hash(self,array):
        dataInstance = Image.fromarray(array)
        P_HASH= imagehash.phash(dataInstance, hash_size=16).__str__()
        print(P_HASH)
        return P_HASH

    def get_features(self,data,color,rate):
        features_list=[lib.feature.mfcc(y=data.astype('float64'),sr=rate),
               lib.feature.melspectrogram(y=data,sr=rate,S=color),
               lib.feature.chroma_stft(y=data,sr=rate,S=color)]
        print(features_list)
        return features_list

    def get_similarity_indexes(self):
        logger.info("get similarity index")
        self.all_similarity_index = similarity_indexes(self.DataBase_songs,self.hashes)
        

        print(self.all_similarity_index)
        
        
    
      

app = QtWidgets.QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec_())

