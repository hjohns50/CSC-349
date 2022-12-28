from ctypes import alignment
import sys

dic = {"A":0, "C":1, "G":2, "T":3, "-":4}
score = []
table = []
answer_str = []
def get_score(seq1, seq2):
    for i in range(len(seq2)):
        table.append([0]*len(seq1))
    #table[2][3] = 1
    for i in range(len(seq2)):
        #print(score[dic[seq2[i]]][0])
        table[i][0] = max(table[i-1][0], score[dic[seq2[i]]][dic[seq1[0]]], score[dic["-"]][dic[seq2[i-1]]])
    for j in range(len(seq1)):
        table[0][j] = max(table[0][j-1], score[dic[seq2[0]]][dic[seq1[j]]], score[dic["-"]][dic[seq1[j-1]]])
    
    for i in range(1, len(seq2)):
        for j in range(1, len(seq1)):
            match = table[i-1][j-1] + score[dic[seq2[i]]][dic[seq1[j]]]
            shift1 = table[i-1][j] + score[dic["-"]][dic[seq2[i]]]
            shift2 = table[i][j-1] + score[dic[seq1[j]]][dic["-"]]
            #print(match, shift1, shift2)
            table[i][j] = max(match, shift1, shift2)
            #for t in table:
                #print(t)
    for i in table:
        print(i)
    return (table[len(seq2)-1][len(seq1)-1])

def get_alignment(seq1, seq2):
    str1 = ""
    str2 = ""
    remaining1 = len(seq1)-1
    remaining2 = len(seq2)-1
    while remaining1 >= 0 and remaining2 >= 0:
        curr = table[remaining2][remaining1]
        diag = table[remaining2-1][remaining1-1]
        above = table[remaining2][remaining1-1]
        left = table[remaining2-1][remaining1]

        
        if(curr == diag + score[dic[seq2[remaining2]]][dic[seq1[remaining1]]]):
            str1 += seq1[remaining1]
            str2 += seq2[remaining2]
            remaining2 -= 1
            remaining1 -= 1
            continue
        elif(curr == above + score[dic[seq1[remaining1]]][dic["-"]]):
            str2 += "-"
            str1 += seq2[remaining2]
            remaining1 -= 1
            continue
        elif( curr == left + score[dic[seq2[remaining2]]][dic["-"]]):
            str1 += "-"
            str2 += seq2[remaining2]
            remaining2 -= 1
            continue
        #print(curr)
        
    while remaining1 >= 0:
        str1 += seq1[remaining1]
        str2 += "-"
        remaining1 -= 1

    while remaining2 >= 0:
        str1 += "-"
        str2 += seq2[remaining2]
        remaining2 -= 1

    str1 = str1[::-1]
    str2 = str2[::-1]
    answer_str.append(str1)
    answer_str.append(str2)

   
def main():
    file = open(str(sys.argv[-1]), "r")
    contents = file.readlines()
    #setup scoring matrix
    for i in range(len(contents)):
        if i == 0:
            seq1 = contents[0].strip("\n")
        if i == 1:
            seq2 = contents[1].strip("\n")              
        if i > 2:
            score.append(contents[i])
    for i in range(len(score)):
        score[i] = score[i].rstrip("\n")
        score[i] = score[i].split(" ")
    for i in range(len(score)):
        for j in range(1, len(score[i])):
            score[i][j] = int (score[i][j])
        score[i] = score[i][1:]
        #print(score[i])
    best = get_score(seq1, seq2)
    get_alignment(seq1, seq2)
    print("x: ", end="")
    for i in range(len(answer_str[0])):
        if i < len(answer_str[0])-1:
            print(answer_str[0][i] + " ", end="")
        else:
            print(answer_str[0][i])
    print("y: ", end="")
    for i in range(len(answer_str[1])):
        if i < len(answer_str[1])-1:
            print(answer_str[1][i] + " ", end="")
        else:
            print(answer_str[1][i])
    #print(answer_str[0])
    #print(answer_str[1])
    print("Score: " + str(best))
if __name__ == "__main__":
    main()
