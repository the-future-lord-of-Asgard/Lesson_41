#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# def strcounter(s):# - O(N*N), т.е. O(N^2) == O(5*5) == O(25)
#     for el in s:
#         counter = 0
#         for sub_el in s:
#             if sub_el == el:
#                 counter += 1
#         print(el, counter)

# strcounter('abbcd')

# def strcounter(s):# - O(M*N), т.е. O(4*5) == O(20)
#     for el in set(s):
#         counter = 0
#         for sub_el in s:
#             if sub_el == el:
#                 counter += 1
#         print(el, counter)

# strcounter('abbcd')# 


# In[ ]:


def strcounter(s):#O(M+N) == O(9)
    el_counter = {}
    for el in s:
        el_counter[el] = el_counter.get(el, 0) + 1# 5 операций
    for el, count in el_counter.items():
        print(el, count)# 4 операций

strcounter('abbcd')


# In[ ]:


# тип множество?
print(set('abbcd'))

