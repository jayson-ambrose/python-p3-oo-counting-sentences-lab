#!/usr/bin/env python3

class MyString:

  def __init__ (self,value=""):
    self.value = value

  def get_value (self):
    return self._value
  
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence (self):
    if self.value[len(self.value) - 1] == '.':
      return True
    else:
      return False

  def is_question (self):
    if self.value[len(self.value) - 1] == '?':
      return True
    else:
      return False

  def is_exclamation (self):
    if self.value[len(self.value) - 1] == '!':
      return True
    else:
      return False

  def count_sentences (self):
    string = self.value
    for p in ["!", "?"]:
      string = string.replace(p, '.')

    sentences = [s for s in string.split(".") if s]

    return len(sentences)

  

  value = property(get_value, set_value)




  
  pass
