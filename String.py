#!/usr/bin/env python
# coding: utf-8

# <h2>Input output</h2>

# In[4]:


bil1 = input ('Isikan bilangan 1 :')
bil2 =  input ('Isikan bilangan 2 :')
hasil = int(bil1) + int (bil2) 
print("Hasil dari", bil1, "+", bil2, "=", hasil)


# In[10]:


p = input ('masukan panjang persegi :')
l = input ('masukan lebar persegi:')
hasil1 = int(p) * int(l)
hasil2 = int (p) + int (l)
print ("Luas persegi panjang adalah", p, "*", l, "=", hasil1)
print ("keliling persegi panjang adalah", p, "+", l, "=", hasil2)


# <h2> Cara Melakukan print dengan menambah end di akhir</h2>

# In[13]:


print ("A","B","C","D", sep='\n', end = "^_^")


# <h2> Memformat dengan index</h2>

# In[20]:


num_1 = 8
num_2 = 10
#hasiul dari 8 modulud 10 = 8
#str.format ()

print ('hasil dari {} modulus {} = {}'. format(num_1,num_2,num_1%num_2))


# <h2>Memformat dengan key</h2>

# In[22]:


fname = "Rizal"
mname = "Dasep"
iname = "alludin"

print ('nama anda {1} {0} {2}'. format (fname,mname,iname))


# <h2>Format tanda pengenal</h2>

# In[24]:


print ('Nama anda {nama},Nilai anda {nilai}'.format (nama = 'Dasep', nilai=100))


# <h2> Pengenalan String</h2>

# In[32]:


univ = "Universitas Nusa Putra"
print ("karakter pertama :", univ [0])
print ("karakter terakhir :", univ [-1])

#universitas
print(univ[0:11])
print(univ[-5:])
print(univ[15:])
print(univ[::-1])


# In[42]:


f_name = 'Rudi'
i_name = 'Andri'

print(f'Nama saya {f_name} {i_name}')

first = 100
second = 20

print(f'Hasil penjumlahan {first} + {second} = {first+second}')


# <h2> Fungsi String</h2>

# In[46]:


nama = "Dasep, Budi, Chika"
nama2 = "Dasep, Budi, Chika"
#split -> memissahkan string berdasarkan karaktrer tertentu
print(nama2.split())
print(nama.split(','))

#join -> Menggabungkan string ke dalam kumpulan karakter
print('@'.join(nama.split(',')))

#input tgl Lahir -> 18/Oktober/2010
#input nama -> Bill Gate
#output:
#Tgl: 18, Bulan: Oktober Tahun: 2010
#Nama Inisial : BG


# In[67]:


tgl = input ("Masukan Tanggal Lahir : ")
nama = input ("Masukan Nama : ")
pemisah = tgl.split("/")
print(f"tgl : {pemisah[0]}, Bulan : {pemisah[1]}, Tahun : {pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"Nama Inisial : {nama_pertama[0]}+{nama_terakhir[0]}")

