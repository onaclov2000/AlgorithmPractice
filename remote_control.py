#!/usr/bin/python -B
################################################################################
# @Title: remote_control.py
#
# @Author: Tyson Bailey
#
# @Date: Sat, 12-Apr-14 08:17AM
#
#
################################################################################
# Basically you have a remote control that is 
#  a, b, c, d, e,
#  f, g, h, i, j,
#  k, l, m, n, o,
#  p, q, r, s, t,
#  u, v, w, x, y,
#  z
# output a list of up down left right commands that will get you to each letter
# Results. This one looks like it works well, however in this implementation there are a few assumptions.
# 1. Hitting left or right will let you reach the respective previous or next line, 
#    I.E. going from k you can hit left and it will go to j.
# 2. Adding new chars will always be in incerasing ordinal value. (since I went a mod and divide route)
# 3. Adding new chars will follow the 5 per line order I did make it a little more generic, so you pass
#    in the width
#
# Note: if a number is less than 5 away from the next/previous, the program will
#       default to hitting left or right the number of times.
#       I.E. z to x is LEFT LEFT SELECT instead of UP RIGHT RIGHT RIGHT SELECT
#
# Source: The original location I found this problem was here:
#         http://www.careercup.com/question?id=5127611667709952
#         it seems to be a relatively short implementation, and you only have a runtime 
#         matching the number of letters passed in, so worst case for a large enough
#         data set I believe it's n runtime. However I don't see how you can get
#         this limitation since you have to look at each letter at least once.
#################################################################################

import sys

def remote_control(word,width):
   from_char = 'a'
   print word
   for i in list(word):
      directions(i.lower(),from_char,width)
      from_char = i.lower()
      
      
def directions(to_c,from_c,width):
   print from_c + "->" + to_c
   print str(ord(from_c)) + "->" + str(ord(to_c))
   if to_c == from_c:
      print "Select"
   elif ord(to_c) > ord(from_c):
      (down_count, right_count) = divmod(ord(to_c) - ord(from_c),width)
      print down_count * "Down ", right_count * "Right ", "Select"
   else:
      (up_count, left_count) = divmod(ord(from_c) - ord(to_c),width)
      print up_count * "Up ", left_count * "Left ", "Select"
   return

if __name__ == "__main__":
   remote_control("TYSONZB",5)
   
   remote_control("ZYZ",5)
   
   remote_control("up",5)
   
   remote_control("hello",5)
   
   remote_control("movie",5)
   
   remote_control("ZZRPG",5)


# sample output.
#
#TYSONZB
#a->t
#97->116
#DownDownDown RightRightRightRight Select
#t->y
#116->121
#Down  Select
#y->s
#121->115
#Up Left Select
#s->o
#115->111
# LeftLeftLeftLeft Select
#o->n
#111->110
# Left Select
#n->z
#110->122
#DownDown RightRight Select
#z->b
#122->98
#UpUpUpUp LeftLeftLeftLeft Select
