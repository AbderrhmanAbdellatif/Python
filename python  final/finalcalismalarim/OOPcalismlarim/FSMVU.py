# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:01:33 2018

@author: Aizen
"""
class ogrenci:
    ogrencicot=0
    def __init__(self,adi,soyadi,ogrenciNo):
        self.adi=adi
        self.soydi=soyadi
        self.ogrenciNo=ogrenciNo
        ogrenci.ogrencicot+=1
    @property 
    def email(self):
        return self.adi[0].upper()+"."+self.soydi+"@"+"fsm.edu.tr"
    @property 
    def full_name(self):
        return self.adi+"  "+self.soydi
    @full_name.setter
    def full_name(self,full):
         self.adi,self.soydi=full.split()
    def apply_raise(self):
        self.ogrenciNo=self.ogrenciNo*2
    @classmethod
    def set_ogrenciNo(ogrenciAdi,ogrencino):    
        ogrenciAdi.ogrenciNo=ogrencino
    @classmethod
    def from_string (cls,emp_str):
        adi,soyadi,ogrenciNo=emp_str.split('-')
        return cls(adi,soyadi,ogrenciNo)
    @staticmethod
    def FSMVU_ogrenci_sayisi():
        return ogrenci.ogrencicot
    def __repr__(self):
        return   "ogrenci"+self.adi+"  "+self.soydi+" no "+str(self.ogrenciNo)
class ucsinif(ogrenci):
        def __init__(self,ogrencAdi,ogrenciSoyadi,ogrenciNo,sinif):
            self.sinif=sinif
            super().__init__(ogrencAdi,ogrenciSoyadi,ogrenciNo)
            