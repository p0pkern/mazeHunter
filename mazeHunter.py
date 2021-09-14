def BFS(arr, color):
    """
    Performs a Breadth First Search on the grid attached to gui.py.
    Takes the dictionary array with the data of all the grid items
    as well as the function that will adjust the colors.
    """

    # Searches the array for the start postion colored green.
    queue = []
    for i in arr:
        if arr[i]["color"] == "green":
            queue.append(arr[i])

    # Performs the BFS functions utilizing the colors of the dictionary items
    while queue:
        s = queue.pop(0)
        # If the color of the current item is not black (barrier), not blue (already visited), and not red (the end)
        if s["color"] != "black" and s["color"] != "blue" and s["color"] != "red":
            # Don't change the starting position to blue
            if s["color"] != "green":
                s["color"] = "blue"

            # Add the grid objects to the queue in the order of top, bottom, left, and right
            if s["top"] is not None and (arr[s["top"]]["color"] != "green" or arr[s["top"]]["color"] != "blue"):
                queue.append(arr[s["top"]])
            if s["bottom"] is not None and (arr[s["bottom"]]["color"] != "green" or arr[s["bottom"]]["color"] != "blue"):
                queue.append(arr[s["bottom"]])
            if s["left"] is not None and (arr[s["left"]]["color"] != "green" or arr[s["left"]]["color"] != "blue"):
                queue.append(arr[s["left"]])
            if s["right"] is not None and (arr[s["right"]]["color"] != "green" or arr[s["right"]]["color"] != "blue"):
                queue.append(arr[s["right"]])
            color(s["id"])

        # Exit if we find the end.
        if s["color"] == "red":
            return
    
def DFS(arr, color):
    """
    Performs a depth first search of the grid. 
    Takes in the dictionary array object, and the function that updates the color
    """

    # Find the start position that is labeled green
    stack = []
    for i in arr:
        if arr[i]["color"] == "green":
            stack.append(arr[i])

    # The main Depth first search function
    while stack:
        s = stack.pop()
        # If the color of the current item is not black (barrier), not blue (already visited), and not red (the end)
        if s["color"] != "black" and s["color"] != "blue" and s["color"] != "red":
            if s["color"] != "green":
                s["color"] = "blue"
            
            # Add the grid objects to the stack in the order of top, bottom, left, and right
            if s["top"] is not None and (arr[s["top"]]["color"] != "green" or arr[s["top"]]["color"] != "blue"):
                stack.append(arr[s["top"]])
            if s["bottom"] is not None and (arr[s["bottom"]]["color"] != "green" or arr[s["bottom"]]["color"] != "blue"):
                stack.append(arr[s["bottom"]])
            if s["left"] is not None and (arr[s["left"]]["color"] != "green" or arr[s["left"]]["color"] != "blue"):
                stack.append(arr[s["left"]])
            if s["right"] is not None and (arr[s["right"]]["color"] != "green" or arr[s["right"]]["color"] != "blue"):
                stack.append(arr[s["right"]])
            color(s["id"])
            
        # Exit if we find the end.
        if s["color"] == "red":
            return