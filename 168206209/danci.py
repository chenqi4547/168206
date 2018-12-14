# -*- coding: utf-8 -*-
start='hit'
end='cog'
paths=['hot','dog','lot','dot','log']
visited=[]
def find_path(start,end,paths):
    if start==end:
        return "start=end"
    else:
        visited.append(start)
        for word in visited:
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    change_word = word[:i]+chr(j)+word[i+1:]
                    if change_word==end:
                        visited.append(end)
                        print(visited)
                        return
                    if change_word in paths and change_word not in visited:
                        visited.append(change_word)
                        print(change_word)
                    
 
                
find_path(start, end, paths)
