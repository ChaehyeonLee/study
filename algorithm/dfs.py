#Depth First Search(DFS; 깊이우선탐색) method
#visited node를 체크함, cycle이 있는 경우에도 무한루프에 빠지지 않음
#tree 전체를 탐색하려면 goal에 None을 넣고, target node가 있는 경우는 그 값을 goal에 넣으면 된다.
def dfs(tree, root, target):
    visited = [] #방문한 node들이 순서대로 visited리스트에 들어간다. dfs한 결과를 나타냄
    stack = [root] ##방문할 node들이 stack에 저장됨. 먼저 root node를 stack에 넣음
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == target: #target node를 찾으면 탐색을 중지함
                return visited #root node부터 target node까지의 dfs 결과를 반환함
            neighbor = tree.get(node) #현재 node의 neighbor node를 받아옴
            if neighbor:
                stack.extend(neighbor)
    return visited #root node부터 tree 전체를 dfs한 결과를 반환함


#-----------------------------------#
# dfs(tree, root, target) method를 테스트하기 위한 tree
test_tree = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G'],
             'E': ['C'], 'F':['C'], 'G': ['D']}

#-----------------------------------#
# dfs(tree, root, target) method 테스트
print('# DFS Tests #')
print('test1_output:', dfs(test_tree, 'A', None)) #'A'를 root node로 test_tree 전체를 dfs
print('test2_output:', dfs(test_tree, 'B', 'C')) #'B'를 root node로 'C'를 찾을 때 까지 dfs 
print('test3_output:', dfs(test_tree, 'C', 'C')) #root node와 target node가 같을 때도 잘 동작함

#-----------------------------------#
#cycle이 있는 경우 동작 테스트
#'D','G','H' node 간에 cycle이 있음
cycle_test_tree = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G', 'H'],
                   'E': ['C'], 'F':['C'], 'G': ['D','H'], 'H': {'D', 'G'}}

print('cycle_test_output:', dfs(cycle_test_tree, 'A', None)) ##cycle이 있는 경우에도 잘 동작함