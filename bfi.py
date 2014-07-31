#!/usr/bin/env python
#
# The Brainf*ck interpreter
#
# The syntax of Brainf*ck
#
# > -- Increment the pointer.
# < -- Decrement the pointer.
# + -- Increment the byte at the pointer.
# - -- Decrement the byte at the pointer.
# . -- Output the byte at the pointer.
# , -- Input a byte and store it in the byte at the pointer.
# [ -- Jump forward past the matching ] if the byte at the pointer is zero.
# ] -- Jump backward to the matching [ unless the byte at the pointer is zero.
#
#
##################################################

import sys

class Brainf_ck:
  def __init__(self, size=30000):
    if size < 0:
      size = 0
    self.size = size
    self.p = 0
    self.a = [0] * size

  def get_value(self):
    return self.a[self.p]

  def i_ptr(self):
    self.p += 1
    if self.p >= self.size:
      self.a.append(0)
      self.size = self.p + 1

  def d_ptr(self):
    self.p -= 1
    if self.p < 0:
      print("Stack underflow!")
      sys.exit(1)

  def i_byte(self):
    self.a[self.p] += 1

  def d_byte(self):
    self.a[self.p] -= 1

  def output(self):
    sys.stdout.write(chr(self.a[self.p]))

  def input(self):
    s = sys.stdin.read()
    self.a[self.p] = ord(s[0])  # read only 1 character


class BFI:
  def __init__(self):    
    self.bf = Brainf_ck()

  def j_forward(self, s, i):
    if self.bf.get_value() == 0:
      n = len(s)
      while True:
        i += 1
        if i >= n:
          print("parse error: does not exist ']'")
          exit(1)
        elif s[i] == "]":
          break
    return i

  def j_backward(self, s, i):
    if self.bf.get_value() != 0:
      while True:
        i -= 1
        if i < 0:
          print("parse error: does not exist '['")
          exit(1)
        elif s[i] == "[":
          break
    return i

  def interpret(self, s):
    i = -1
    n = len(s)
    while True:
      i += 1
      if i >= n:
        break
      c = s[i]
      if c == ">":
        self.bf.i_ptr()
      elif c == "<":
        self.bf.d_ptr()
      elif c == "+":
        self.bf.i_byte()
      elif c == "-":
        self.bf.d_byte()
      elif c == ".":
        self.bf.output()
      elif c == ",":
        self.bf.input()
      elif c == "[":
        i = self.j_forward(s, i)
      elif c == "]":
        i = self.j_backward(s, i)


# main process
# arguments
arg = sys.argv[1:]

# Brainf_cker
bfi = BFI()

for fn in arg:
  try:
    f = open(fn, 'r')
  except IOError:
    print("file does not exist: {}".format(fn))
  else:
    #print("file: {}".format(fn))
    s = f.read()
    f.close()
    bfi.interpret(s)

