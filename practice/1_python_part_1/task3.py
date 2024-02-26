"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable

def build_from_unique_words(*lines,word_number):
  new_str=''
  unique=''
  line=0
  for each in lines:
      count=0
      for i in each.split(" "):
          if((line==0 and isinstance(i, str)) or line==1 or line==2):
            if(unique==i):
              continue  
            else:
               if count==word_number:
                  new_str+=i+" "
          count+=1
          unique=i
      line+=1      
  print(new_str)          
build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk',word_number=1) 


