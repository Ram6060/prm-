#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
lst = []
for i in range(n):
    s = input().strip()
    lst.append(s)

sorted_lst = sorted(lst, key=lambda x: x[-2])

print(sorted_lst)

