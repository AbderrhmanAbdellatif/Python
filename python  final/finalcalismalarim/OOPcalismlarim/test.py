# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:01:45 2018

@author: Aizen
"""

from FSMVU import ogrenci
from FSMVU import ucsinif 
birincio=ogrenci("Abderhman","Abdellatif",1421221042)
ikincio=ogrenci("ENSE","TURNC",145897547)
print(birincio.email)
print(birincio.full_name)
print(ikincio.email)
birincio.full_name="omar gad"
print(birincio.full_name)
print(birincio.ogrenciNo)
birincio.apply_raise()
print(birincio.ogrenciNo)
mystr="Abderrhman-Abdellatif-14569872"
Adi,soyadi,No=mystr.split('-')
ucuncuo=ogrenci(Adi,soyadi,No)
print(ucuncuo.full_name)
ucuncuo.apply_raise()
print(ucuncuo.ogrenciNo)
print(ucuncuo.FSMVU_ogrenci_sayisi())
print(ucuncuo.__dict__)
fsmvuogrenci=ucsinif("lbderrhman","Abdellatif",1421221042,3)
print(fsmvuogrenci.email)