#!/usr/bin/env python
# coding: utf-8

# <h2>Operator Aritmatika</h2>

# In[1]:


num1 = 10
num2 = 3

jumlah = num1 + num2
kurang = num1 - num2
kali = num1 * num2
bagi = num1 / num2
bagi_bulat = num1 // num2
pangkat = num1 ** num2
modulus = num1 % num2

print(jumlah)
print(kurang)
print(kali)
print(bagi)
print(bagi_bulat)
print(pangkat)
print(modulus)


# <h2>Operator Penugasan</h2>

# In[13]:


x  = 5 #assigment operator
x +=10 # x = x +10=>15
print (x)
x -=4 # x = X - 4 =>11
print(x)
x *=2 # x = x * 2 =>22
print(x)
x /=3 # x = x / 3 =>7...
print(x)
x //=2 # x = x // 2 =>3.0
print(x)
x **=3 # x = x ** 3 =>27.0
print(x)
x %=2 # x = % 2 =>1
print(x)


# <h2>Operator Perbandingan</h2>

# In[20]:


bil1 = 8
bil2 = 7

is_equal = bil1 == bil2
is_not_equal = bil1 != bil2
is_greater_than = bil1 > bil2
is_less_than = bil1 < bil2
is_greater_equal = bil1 >= bil2
is_less_equal = bil1 <= bil2

print(is_equal)
print(is_not_equal)
print(is_greater_than)
print(is_less_than)
print(is_greater_equal)
print(is_less_equal)


# <h2>Operator Logika</h2>

# In[23]:


var1 = 4
var2 = 10

opr_and = var1 < var2 and var1 <=4 #True
opr_or = var1 >=var2 or var1 % 2==1 #False
opr_not = not opr_or

print(opr_and)
print(opr_or)
print(opr_not)


# <h2>Operator Identitas</h2>

# In[32]:


fruits = ["apple", "mangga", "watermelon"]
my_favorite_fruits = fruits
your_fruits = ["apple","mangga","watermelon"]

print(fruits is my_favorite_fruits)
print(fruits is my_favorite_fruits)
print(fruits is not my_favorite_fruits)
print(fruits is not your_fruits)


# <h2>Operator Keanggotaan</h2>

# In[36]:


student_name = ["Andi","Beni","Chika"]
print("Beni" in student_name)
print("andi" not in student_name)


# <h2>Operator Bitwise</h2>

# In[40]:


nilai_and = 255 & 15
nilai_or = 255 | 15
nilai_xor = 255 ^ 15
#11111111
#00001111
#--------xor
#00001111 => 16 + 32 +64 +128
print(nilai_and)
print(nilai_or)
print(nilai_xor)

