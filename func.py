import sys, time, color,os,random
os.system("pip3 install getch")
import getch
os.system("clear")
def intro():
  input("Stretch those fingers for me! And break a thumb! \nPress [ENTER] to begin...")
  print("3...")
  time.sleep(1)
  print("2...")
  time.sleep(1)
  print("1...")
  time.sleep(1)
  print("Start!")
  time.sleep(1)
  os.system("clear")
def practice(string:str):
    intro()
    result = typingtest(string)
    wpm = round((result[2]/5)/(result[1]/60))
    score = round(wpm/result[0])*10
    print(f"The practice has finished here are your results!")
    print("Wpm: ",wpm)
    print("Score: ",score)
    return [result[0], result[1]]
def test(*args):
  length = random.randint(30,40)
  alllet = [' ']
  nospace = []
  for arg in args:
    alllet.append(arg)
    nospace.append(arg)
  for i in range(round((len(alllet)-1)/4)):
    alllet.append(" ")
  x = alllet[1]+""
  y = alllet[1]+""
  for i in range(length):
    x+=random.choice([alllet[0],alllet[1],alllet[2]])
    y+=random.choice(alllet)
  for i in range(round(length/4)):
    y+=random.choice(alllet)
  x+=alllet[1]
  y+=alllet[2]
  ranlist = x.split()
  ranlist2 = y.split()
  y=""
  x = ""
  for i in range(len(ranlist)):
    if i != len(ranlist)-1:
      x+=ranlist[i]+" "
    else:
      x+=ranlist[i]
  del i
  for i in range(len(ranlist2)):
    if i != len(ranlist2)-1:
      y+=ranlist2[i]+" "
    else:
      y+=ranlist2[i]
  while True:
      type(f"Our next letters are going to be [{alllet[1]}] and [{alllet[2]}] ")
      practice(x)
      type("Ok! Good you made it throught the practice now its time for the test! Remember to take the test carefully. If you make more than five mistakes you will have to practice again. If your WPM is lower than 8 then you will have to take the test again...")
      input("[PRESS ENTER] to Continue")
      result = practice(y)
      if result[0] > 5 or result[1] < 8:
        type("Well lets try to focus! Lets do the practice again to strengthen your hand muscles!")
        continue
      else:
        type("Good you made it through!")
        break
  return [result[0],result[1]]
def type(string:str, wait:int = 0.02):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(wait)
  print()
def typingtest(paragraph):
  splitparagraph = []
  mistakes = 1
  length = 0
  mist = {}
  for char in paragraph:
    splitparagraph.append(char)
    mist[length] = 0
    length+=1
  currentchar = 0
  original = splitparagraph.copy()
  start = time.time()
  while currentchar < length:
    print(*splitparagraph,sep="")
    letter = getch.getch()
    print("\033[H",end="")
    if letter == original[currentchar]:
      splitparagraph[currentchar] = color.green +color.underline+ original[currentchar] + color.white
      currentchar+=1
    else:
      mist[currentchar]+=1
      mistakes+=1
      if mist[currentchar] > 2:
        splitparagraph[currentchar] = color.red + color.reverse+ original[currentchar] + color.white
      else:
        splitparagraph[currentchar] = color.red + color.bold+ original[currentchar] + color.white
    if currentchar == len(original):
      break
  timeing = time.time() - start
  print(*splitparagraph,sep="")
  return [mistakes,timeing,length]