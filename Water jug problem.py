def waterJugProblem(jug1Cap, jug2Cap, targetAmount):    
    j1 = 0    
    j2 = 0    
    actions = [("fill", 1), ("fill", 2), ("empty", 1), ("empty", 2), ("pour", 1, 2), ("pour", 2, 1)]       
    visited = set()    
    queue = [(j1, j2, [])]      
    while queue:      
        j1, j2, seq = queue.pop(0)        
        if (j1, j2) not in visited:    
            visited.add((j1, j2))       
            if j1 == targetAmount or j2 == targetAmount:    
                return seq        
            for action in actions:    
                if action[0] == "fill":    
                    if action[1] == 1:    
                        next_state = (jug1Cap, j2)    
                    else:    
                        next_state = (j1, jug2Cap)    
                elif action[0] == "empty":    
                    if action[1] == 1:    
                        next_state = (0, j2)    
                    else:    
                        next_state = (j1, 0)    
                else:     
                    if action[1] == 1:    
                        amount = min(j1, jug2Cap - j2)    
                        next_state = (j1 - amount, j2 + amount)    
                    else:    
                        amount = min(j2, jug1Cap - j1)    
                        next_state = (j1 + amount, j2 - amount)        
                if next_state not in visited:    
                    next_seq = seq + [action]    
                    queue.append((next_state[0], next_state[1], next_seq))         
    return None    
result = waterJugProblem(4, 3, 2)    
print(result)  
