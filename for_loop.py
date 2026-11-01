strs = ["flower", "flow", "flight"]

def main():
    for i in range(len(strs[0])):

        char = strs[0][i]

        for s in strs[1:]:
            if i > len(s) or s[i] != char:
                return(strs[0][:i])

            
print(main())