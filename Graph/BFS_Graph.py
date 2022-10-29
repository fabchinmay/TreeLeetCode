def main(args):
    adj = []
    for i in range(0, 5):
        adj.append([])


    adj[0].append(1)
    adj[1].append(0)
    adj[0].append(2)
    adj[2].append(0)
    adj[0].append(3)
    adj[3].append(0)
    adj[2].append(4)
    adj[4].append(2)

    adjj = [[] for _ in range(5)]
    adjj[0].append(1)
    adjj[1].append(0)
    adjj[0].append(2)
    adjj[2].append(0)
    adjj[0].append(3)
    adjj[3].append(0)
    adjj[2].append(4)
    adjj[4].append(2)

    print(adj)
    print(adjj)


main(0)