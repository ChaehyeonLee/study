#Breadth First Search(BFS; 너비우선탐색) method
#tree 전체를 탐색하려면 goal에 None을 넣고, target node가 있는 경우는 그 값을 goal에 넣으면 된다.
def bfs(tree, root, target):
    visited = [] #방문한 node들이 순서대로 visited리스트에 들어간다. bfs할 때의 탐색 순서를 나타냄
    queue = [root] #방문할 node들이 queue에 저장됨. 먼저 root node를 queue에 넣음
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == target: #target node를 찾으면 탐색을 중지함
                return visited #root node부터 target node까지의 bfs 순서를 반환함
            neighbor = tree.get(node) #현재 node의 neighbor node를 받아옴
            if neighbor:
                queue.extend(neighbor)
    if target != None:
        print("Couldn't find the target")
        
    return visited #root node부터 tree 전체를 bfs 순서를 반환함


#-----------------------------------#
# bfs(tree, root, target) method를 테스트하기 위한 tree
test_tree = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G'],
             'E': ['C'], 'F':['C'], 'G': ['D']}

#-----------------------------------#
# bfs(tree, root, target) method 테스트
print('# BFS Tests #')
print('test1_output:', bfs(test_tree, 'A', None)) #'A'를 root node로 test_tree 전체를 bfs
print('test2_output:', bfs(test_tree, 'B', 'C')) #'B'를 root node로 'C'를 찾을 때 까지 bfs 
print('test3_output:', bfs(test_tree, 'C', 'C')) #root node와 target node가 같을 때도 잘 동작함
print('test4_output:', bfs(test_tree, 'C', 'H')) #target을 찾지 못했을 때도 잘 동작함