def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n-1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n-1, helper, source, target)
        
source = [37,36,30,26,22,19,16,12,8,3,1]
target = []
helper = []
print("Initially:\n")
print("Source=",source, "Helper=",helper, "Target=",target,"\n\n\n")
hanoi(len(source),source,helper,target)
print("After processing Hanoi:\n")
print("Source=",source, "Helper=",helper, "Target=",target,"\n\n\n")
