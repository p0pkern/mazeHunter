import threading

def BFS(arr, color):
    
    queue = []
    for i in arr:
        if arr[i]["color"] == "green":
            queue.append(arr[i])

    while queue:
        s = queue.pop(0)
        if s["color"] != "black" and s["color"] != "blue" and s["color"] != "red":
            if s["color"] != "green":
                s["color"] = "blue"

            if s["top"] is not None and (arr[s["top"]]["color"] != "green" or arr[s["top"]]["color"] != "blue"):
                queue.append(arr[s["top"]])
            if s["bottom"] is not None and (arr[s["bottom"]]["color"] != "green" or arr[s["bottom"]]["color"] != "blue"):
                queue.append(arr[s["bottom"]])
            if s["left"] is not None and (arr[s["left"]]["color"] != "green" or arr[s["left"]]["color"] != "blue"):
                queue.append(arr[s["left"]])
            if s["right"] is not None and (arr[s["right"]]["color"] != "green" or arr[s["right"]]["color"] != "blue"):
                queue.append(arr[s["right"]])
            color(s["id"])
            
        if s["color"] == "red":
            return
    
