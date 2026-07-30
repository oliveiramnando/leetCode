class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathSplit = path.split('/')

        i = 0
        n = len(pathSplit)


        for p in pathSplit:
            if stack and p == '..':
                stack.pop()
            elif p == '' or p == '.' or p == '..':
                pass 
            else: 
                stack.append(p)
            i += 1
    
        simPath = '/'.join(stack)

        return '/' + simPath
