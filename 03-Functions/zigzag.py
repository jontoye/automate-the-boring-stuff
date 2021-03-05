import time, sys

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indent_increasing:
            # Increase number of spaces
            indent += 1  
            if indent == 20:
                # Change direction
                indent_increasing = False

        else:
            # Decrease number of spaces
            indent -= 1
            if indent == 0:
                # Change direction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
