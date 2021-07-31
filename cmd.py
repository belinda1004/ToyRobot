'''
Check and execute commands
'''

def proc_cmd(robot):
    command_str = input("Command: ")
    command_list = command_str.split(" ")
    command = command_list[0].upper()

    if not command in ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]:
        print("Unknown command.")
        return

    if (len(command_list) > 1 and command != "PLACE") or \
            (len(command_list) < 2 and command == "PLACE"):
        print("Invalid arguments.")
        return

    if command == "PLACE":
        try:
            x, y, facing = "".join(command_list[1:]).split(",")
            x = int(x)
            y = int(y)
        except ValueError:
            print("Invalid arguments.")
            return
        result = robot.place(x, y, facing)
    elif command == "MOVE":
        result = robot.move()
    elif command == "LEFT":
        result = robot.left()
    elif command == "RIGHT":
        result = robot.right()
    else:  # REPORT
        result = robot.report()
    print(result)
    return

