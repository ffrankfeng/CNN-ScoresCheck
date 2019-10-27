import  numpy
# ans =numpy.array([
# [[0, 0.94785792], [2, 0.024368588], [9, 0.012735714],[9, 0.012735714]],
# [[1, 0.63692123], [5, 0.2041491], [6, 0.11921614],[9, 0.012735714]],
# [[2, 0.71904856], [5, 0.16892526], [8, 0.040210374],[9, 0.012735714]],
# [[3, 0.57939857], [8, 0.16285999], [9, 0.084402792],[9, 0.012735714]],
# [[3, 0.57939857], [8, 0.16285999], [9, 0.084402792],[9, 0.012735714]],
# [[3, 0.57939857], [8, 0.16285999], [9, 0.084402792],[9, 0.012735714]],
#  [[1, 0.71904856], [23, 0.16892526], [17, 0.040210374],[9, 0.012735714]]])

def isExist(count,ans):
    flag = False
    for i in range(len(ans)):
        if count == ans[i][0]:
            flag = True
            return i
    if flag == False:
        return -1

def stepRun(i,max,step):
    if i <0:
        return
    if step[i] < max:
        step[i]+=1
    else:
        step[i]=0
        stepRun(i-1,max,step)
def calculation(ans,index):
    ans = numpy.array(ans)

    dimension = ans.shape
    step = [0 for i in range(dimension[0] - 1)]
    x = 0
    for  k in range(pow(dimension[1],dimension[0]-1)):
        count = 0
        for i in range(dimension[0]-1):
            count += ans[i][step[i]][0]
            isExistReturn = isExist(count, ans[dimension[0] - 1])
        if isExistReturn>-1:

            for i in range(len(step)):
                index[x][i] = step[i]
            index[x][i+1] = isExistReturn
            x += 1
        stepRun(dimension[0]-2,dimension[1]-1,step)
