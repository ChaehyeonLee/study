#Depth First Search(DFS; 깊이우선탐색) method
#visited node를 체크함, cycle이 있는 경우에도 무한루프에 빠지지 않음
#graph 전체를 탐색하려면 goal에 None을 넣고, target node가 있는 경우는 그 값을 goal에 넣으면 된다.
#
##해결되지 않은 고민 
##: 'visited' 리스트는 dfs가 실행될 때 노드의 방문 순서가 정확한가를 테스트시에 시각적으로 보기 위해 사용.
##   그러나 dfs를 일반적인 graph에서 사용하기 위해 코드를 작성하다보니 'visited'를 dfs(graph, root, target)함수
##   구현시에 이용했음.
##   'visited'를 이용하지 않고 dfs를 구현할 수는 있으나 함수의 처리과정이 너무 길어짐.
##   처리과정이 길어지는 것보다는 'visited'를 이용함으로서 공간을 더 차지하는 것이 오히려 나은 것 같음.
##   따라서 아래의 코드는 'visited'를 이용하여 dfs 함수를 구현한 것.

def dfs(graph, root, target):
    visited = [] #방문한 node들이 순서대로 visited리스트에 들어간다. dfs할 때의 탐색 순서를 나타냄
    stack = [root] ##방문할 node들이 stack에 저장됨. 먼저 root node를 stack에 넣음
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == target: #target node를 찾으면 탐색을 중지함
                return visited #root node부터 target node까지의 dfs한 순서를 반환함
            neighbor = graph.get(node) #현재 node의 neighbor node를 받아옴
            if neighbor:
                stack.extend(neighbor)

    if target != None:
        print("Couldn't find the target")

    return visited #root node부터 graph 전체를 dfs한 순서를 반환함


#-----------------------------------#
# dfs(graph, root, target) method를 테스트하기 위한 graph
test_graph = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G'],
             'E': ['C'], 'F':['C'], 'G': ['D']}

#-----------------------------------#
# dfs(graph, root, target) method 테스트
print('# DFS Tests #')
print('test1_output:', dfs(test_graph, 'A', None)) #'A'를 root node로 test_graph 전체를 dfs
print('test2_output:', dfs(test_graph, 'B', 'C')) #'B'를 root node로 'C'를 찾을 때 까지 dfs 
print('test3_output:', dfs(test_graph, 'C', 'C')) #root node와 target node가 같을 때도 잘 동작함
print('test4_output:', dfs(test_graph, 'C', 'H')) #target을 찾지 못했을 때도 잘 동작함

#-----------------------------------#
#cycle이 있는 경우 동작 테스트
#'D','G','H' node 간에 cycle이 있음
cycle_test_graph = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G', 'H'],
                   'E': ['C'], 'F':['C'], 'G': ['D','H'], 'H': {'D', 'G'}}

print('cycle_test_output:', dfs(cycle_test_graph, 'A', None)) #cycle이 있는 경우에도 잘 동작함