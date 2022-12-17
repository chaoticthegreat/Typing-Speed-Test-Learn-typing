from func import intro, typingtest,test,type
paragraphs = ['this is the first test it will have no punctuation or numbers it will also have no capitals so let us begin once upon a time on a bright christmas night their was a jolly old fellow named bob bob liked to eat hot chocolate on cold days so he did today he made himself some hot chocolate well this is the ned of the first test bye','Hi this is the 2nd test with numbers and capital included Dont worry rather than going really fast it is better to take your time and focus on not making any mistakes Okay NOW let us begin. Bob had 10 ButterNut Exelsis chocolates and boy did he not like to share them with anyone In fact he almost hit Mayor Hieldgans when he tried to help himself to a piece Bob spend 354 dollars and 49 cents on those choclates They used to 567833 dollars but Bob protested and the company Exelsis made it 500 The story is now done lets HOPE you did WELL on the 2nd TEST', 'Hey there! Welcome to the 2nd test! I\'m a little surpised that you made it this far. Enough talk lets get to the story. One day when Bob was young, one of the stocks that he bought suddenly went up by a lot of points. It was so much points that became rich at the age of 20. Of course spent all the money on expensive stuff like Ferrari\'s. This is the end of the last test! You can now see your results!']
while True:
  choice = input("[TYPE IN THE NUMBER]Do you want to:\n1. Take the Typing Test\n2. Learn to type better\n")
  if choice == '1':
    wpms = []
    scores = []
    for i in range(3):  
      intro()
      result = typingtest(paragraphs[i])
      wpm = round((result[2]/5)/(result[1]/60))
      score = round(wpm/result[0])*10
      wpms.append(wpm)
      scores.append(score)
      print(f"The Test {i} has finished here are your results!")
      print("Wpm: ",wpm)
      print("Mistakes: ",result[0])
      print("Score: ",score)
      input("Press [ENTER] to continue")
    averwpm = (wpms[0]+wpms[1]+wpms[2])/3
    totalscore = (scores[0]+scores[1]+scores[2])*10
    print("Your average WPM is:\n",averwpm)
    print("Your total score is:\n",totalscore)
    break
  elif choice == '2':
    type("Alright by the end of this you will at least have some familarty with a keyboard.")
    type("Keep your fingers on the home row\nIf you don't know what the home row is press this link:\nhttps://www.computerhope.com/jargon/h/hrk.htm")
    type("If this is your first time learning with this appplication all  you have to do is to type what it says on the screen")
    type("Remember that your thumbs stay on the space bar!")
    test("f","j")
    test("k","d","f","j")
    test("s","l","k","d","f","j")
    test("a",";","s","l","k","d","f","j")
    type("Now to type the letters [g] and [h] you will have the extend your index fingers toward them")
    test("g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [t] and [y] you will have the extend your index fingers forward, toward them")
    test("t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [r] and [u] you will have the extend your index fingers forward, toward them")
    test("r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [i] and [e] you will have the extend your middle fingers forward, toward them")
    test("i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [w] and [o] you will have the extend your ring fingers forward, toward them")
    test("w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [q] and [p] you will have the extend your pinkie fingers forward, toward them")
    test("q","p","w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Congrats! You just learned the top row!\nNow for the bottom!\nNow to type the letters [v] and [b] you will have the extend your index fingers under, toward them")
    test("v","b","q","p","w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [n] and [c] you will have the extend your middle fingers under, toward them")
    test("n","c","v","b","q","p","w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [x] and [m] you will have the extend your ring fingers under, toward them")
    test("x","m","n","c","v","b","q","p","w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Now to type the letters [z] and [,] you will have the extend your pinkie fingers under, toward them")
    test("x","m","n","c","v","b","q","p","w","o","i","e","r","u","t","y","g","h","a",";","s","l","k","d","f","j")
    type("Congrats! You have succesfully learned how to type all the letters on the keyboard")
    break
  else:
    continue