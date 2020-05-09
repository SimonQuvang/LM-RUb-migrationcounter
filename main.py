import pyautogui
import time
numberOne = [1240, 445];
numberTwo = [1360, 445];
numberThree = [1490, 445];
numberFour = [1240, 530];
numberFive = [1360, 530];
numberSix = [1490, 530];
numberSeven = [1240, 630];
numberEight = [1360, 630];
numberNine = [1490, 630];
numberZero = [1260, 700];

searchKingdomPos = [870, 160];
kingdomPos = [750, 395];
acceptKingdomNumber = [1500, 720];
goButton = [930, 545];

try:
    time.sleep(5)
    for x in range(1, 10):
        time.sleep(5)
        pyautogui.click(searchKingdomPos[0], searchKingdomPos[1])
        time.sleep(1)
        pyautogui.click(kingdomPos[0], kingdomPos[1])
        numbers = list(map(int, str(x)))
        for item in numbers:
            time.sleep(1)
            if item == 0:
                pyautogui.click(numberZero[0], numberZero[1])
            elif item == 1:
                pyautogui.click(numberOne[0], numberOne[1])
            elif item == 2:
                pyautogui.click(numberTwo[0], numberTwo[1])
            elif item == 3:
                pyautogui.click(numberThree[0], numberThree[1])
            elif item == 4:
                pyautogui.click(numberFour[0], numberFour[1])
            elif item == 5:
                pyautogui.click(numberFive[0], numberFive[1])
            elif item == 6:
                pyautogui.click(numberSix[0], numberSix[1])
            elif item == 7:
                pyautogui.click(numberSeven[0], numberSeven[1])
            elif item == 8:
                pyautogui.click(numberEight[0], numberEight[1])
            elif item == 9:
                pyautogui.click(numberNine[0], numberNine[1])
        time.sleep(1)
        pyautogui.click(acceptKingdomNumber[0], acceptKingdomNumber[1])
        time.sleep(1)
        pyautogui.click(goButton[0], goButton[1])

except KeyboardInterrupt:
    print("Done")
