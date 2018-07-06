#Breadth First Search(BFS; 너비우선탐색) method
#graph 전체를 탐색하려면 goal에 None을 넣고, target node가 있는 경우는 그 값을 goal에 넣으면 된다. 
#
##해결되지 않은 고민 
##: 'visited' 리스트는 bfs가 실행될 때 노드의 방문 순서가 정확한가를 테스트시에 시각적으로 보기 위해 사용.
##   그러나 bfs를 일반적인 graph에서 사용하기 위해 코드를 작성하다보니 'visited'를 bfs(graph, root, target)함수
##   구현시에 이용했음.
##   'visited'를 이용하지 않고 bfs를 구현할 수는 있으나 함수의 처리과정이 너무 길어짐.
##   처리과정이 길어지는 것보다는 'visited'를 이용함으로서 공간을 더 차지하는 것이 오히려 나은 것 같음.
##   따라서 아래의 코드는 'visited'를 이용하여 bfs 함수를 구현한 것.

def bfs(graph, root, target):
    visited = [] #방문한 node들이 순서대로 visited리스트에 들어간다. bfs할 때의 탐색 순서를 나타냄
    queue = [root] #방문할 node들이 queue에 저장됨. 먼저 root node를 queue에 넣음
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == target: #target node를 찾으면 탐색을 중지함
                return visited #root node부터 target node까지의 bfs 순서를 반환함
            neighbor = graph.get(node) #현재 node의 neighbor node를 받아옴
            if neighbor:
                queue.extend(neighbor)
    if target != None:
        print("Couldn't find the target")

    return visited #root node부터 graph 전체를 bfs 순서를 반환함


#-----------------------------------#
# bfs(graph, root, target) method를 테스트하기 위한 graph
test_graph = {'A': ['B', 'C'], 'B':['A', 'D'], 'C':['A', 'E', 'F'], 'D': ['B', 'G'],
             'E': ['C'], 'F':['C'], 'G': ['D']}

#-----------------------------------#
# bfs(graph, root, target) method 테스트
print('# BFS Tests #')
print('test1_output:', bfs(test_graph, 'A', None)) #'A'를 root node로 test_graph 전체를 bfs
print('test2_output:', bfs(test_graph, 'B', 'C')) #'B'를 root node로 'C'를 찾을 때 까지 bfs 
print('test3_output:', bfs(test_graph, 'C', 'C')) #root node와 target node가 같을 때도 잘 동작함
print('test4_output:', bfs(test_graph, 'C', 'H')) #target을 찾지 못했을 때도 잘 동작함