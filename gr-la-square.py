from ast import literal_eval
import sys;
with open(sys.argv[1]) as f:
    mainlist = [list(literal_eval(line)) for line in f]
size = len(mainlist);
print(size);
M = [[0 for x in range(size)] for y in range(size)]
for r in range(0, size):
    for t in range(0, size):
        M[r][t] = mainlist[r][t];
ll = []
lp = [];
solution=[];
def gram(M, x, y, total):
    if x == total or y == total:
        ll.append(lp);
        return 0
    lp.append(M[x][y]);
    gram(M, x + 1, y, total);
tot = [];
def ana(s, la):
    mem = [];
    for x in s:
        for y in la:
            mem.append(x)
            mem.append(y);
            tot.append(mem);
            mem = [];
def ana2(s, la):
    mem = [];
    tot = [];
    for x in s:
        for y in la:
            mem = x[:]
            mem.append(y)
            tot.append(mem);
            mem = [];
    return tot;
def getgram(gr):
    used = [];
    for stili  in range(0, size):
        count = 0;
        for grami in range (0, size):
            if M[grami][stili] == gr[stili]:
                if grami in used:
                    return 0
                else:
                    used.append(grami);
    return 1;
def check(g):
    usn = []
    for x in g:
        if x in usn:
            return 0;
        else:
            usn.append(x);
    gram = getgram(g);
    if gram == 0:
        return 0;
    else:
        return 1;
    return 1;
def find(l, tot, cont):
    tl = [];
    totcoun = 0;
    all = [];
    print(l);
    for i in range(0, size):
        lst = [];
        all.append(lst);
    ct = 0;
    for i in l:
        n = l[ct];
        all[ct].append(n);
        ct = ct + 1;
    cc = 0;
    flag = 1;
    for yy in range (cont, len(tot)):
        lis = tot[yy];
        print(lis);
        if cc != cont:
            ca = 0;
            sos = 0;
            for gr in lis:
                temp=[];
                nn = gr;
                print(nn)
                if nn in all[ca]:
                    flag = 0;
                    print(nn," | ",ca)
                    print(all[ca]);
                    break;
                else:
                    sos = sos + 1;
                    temp.append(nn);
                    print(ca, nn)
                    if (sos == size):
                        for  tt in temp:
                            all[ca].append(tt);
                        print("auto",lis);
                        totcoun = totcoun + 1;
                        tl.append(lis);
                        if totcoun == size-1:
                            tl.append(l)
                            solution=tl[:];
                            return solution;
                ca = ca + 1;
        cc = cc + 1
    return [];
def prod_latin(l):
    t = [[0 for x in range(size)] for y in range(size)]
    for o in range (0,size):
            for p in range(0,size):
                t[o][p]=M[o][p]
    for le in l:
        nu=le[0];
        for o in range (0,size):
            for p in range(0,size):
                if M[p][o]==le[o]:
                    t[p][o]=nu;
    for o in range (0,size):
        for p in range(0,size):
            print(t[o][p], " ",end="");
        print("")
    return t;
for x in range(0, size):
    lp = [];
    gram(M, 0, x, size);
ana(ll[0], ll[1]);
pre = tot;
for ii in range(2, size):
    k = ana2(pre, ll[ii]);
    pre = k
total = [];
for j in k:
    a = check(j)
    if a == 1:
        total.append(j);
print(total)
k=[]
for w in range(0, len(total)):
    k= find(total[w], total, w);
    print(k)
    if len(k)==size:
        print(k)
        break;
fin=prod_latin(k);
for u in range(0,size):
    for y in  range(0,size):
      print("(",M[u][y],",",fin[u][y],") ",end="");
    print("")
    
