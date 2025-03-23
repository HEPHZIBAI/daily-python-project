import time

def set_alaram(hr,min):
    print(f"alaram set for {hr} {min}")
    curr=time.localtime()

    while curr.tm_hour!=hr or curr.tm_min!=min:
        curr=time.localtime()
        time.sleep(30)

    print("time is up wakeup")

set_alaram(10,49)