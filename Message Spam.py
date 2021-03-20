import pyautogui, time
time.sleep(10)
##replace "New Text Document (3).txt" with spam text to be opened##
f = open("New Text Document (3).txt", 'r')
for word in f :
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
    
