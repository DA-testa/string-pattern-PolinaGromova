# python3

def read_input():
    text=input()
    if "F" in text:
        filename = input("Enter file name: ") 
        path = './tests/'
        file=path+filename
        with open("input.txt", mode="r") as f:
                pattern=f.readline().strip()
                text=f.readline().strip()
    elif "I" in text:
        pattern=input().strip()
        text=input().strip()
    else: print("Input error")
    
    return pattern,text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    q = 257  # a prime number to use for hashing
    d = 256  # size of the alphabet
    p_hash=t_hash=0
    
    for i in range(len(pattern)):
        p_hash=(d*p_hash+ord(pattern[i]))%q
        t_hash=(d*t_hash+ord(text[i]))%q
    occurrences=[]
    for i in range(len(text)-len(pattern)+1):
        if p_hash==t_hash and text[i:i+len(pattern)]==pattern:
            occurrences.append(i)
        if i<len(text)-len(pattern):
            t_hash=(d*(t_hash-ord(text[i])*pow(d,len(pattern)-1, q))+ord(text[i+len(pattern)]))%q
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

