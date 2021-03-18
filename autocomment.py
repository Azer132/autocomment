import pyautogui
import time


comments=["#DYNAMIC_NETWORK_CLUBS","#DYNAMIC_MONASTIR_CLUBS","#DYNAMIC_FSM_CLUB","#KEEP_MOVING_FORWARD"]
comment=["#BE_DYNAMIC","#DYNAMIC_FSM"]
time.sleep(5)
for j in range(100):
    
    for i in range (4):
        pyautogui.typewrite(comments[i])
        pyautogui.typewrite("\n")
        time.sleep(3)
    