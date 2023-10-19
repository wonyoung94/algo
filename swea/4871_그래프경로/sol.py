import sys
sts.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V :  노드수, E : 간선수
    V, E = list(map(int, input().split()))

    nodes = [[0 for _ in range(V+1)for _ in range(V+1)]]

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node[0]
        end = node[1]

        nodes[start][end] = 1

    S, G = list(map(int, input().split()))

    # 여기까지가 데이터 받아옴 ( 인풋 데이터는 1-2 연결되있는걸 2차원 배열로 표현)

    # nodes => 그래프 (인접 행렬 방식)

    # 방문 체크리스트
    check_list = [False] * (V+1)

    # dfs용 stack
    stack = []

    # v 부터 시작
    v = S
    check_list[v] = True
    stack.append(v)

    result = 0

    while len(stack):
        for w in range(V+1):
            # 연결된것을 확인 == 1
            if nodes[v][w] == 1:
                # 아직 방문하지 않았다면
                # =>체크리스트가 False라면
                if not check_list[w]:
                    # 나의위치v를 stack에 push
                    stack.append(v)
                    check_list[w] = True

                    # w를 현재 위치로 변경
                    v = w

                    if w == G:
                        result = 1         
                    break
        # break를 만나지 않은경우
        # => 방문하지 않은 정점이 없는경우
        # => 과거의 위치로 돌아가기
        else:
            v = stack.pop()

    print(result)

