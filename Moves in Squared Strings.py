''' 
6 kyu  Python
https://www.codewars.com/kata/56dbe7f113c2f63570000b86

started: 7/2/24
completed: 7/6/24

'''


def rot(strng):
    k=[]
    x=strng.split('\n')
    for i in x[::-1]:
        print(i[::-1])
        k.append(i[::-1])
    return '\n'.join(k)

  

def selfie_and_rot(strng):
    d = [i + "." * len(i) for i in strng.split('\n')]  # Original list with dots
    f = ["." * len(i) + i[::-1] for i in strng.split('\n')[::-1]]  # Reversed list with dots
    processed_list = d + f
    t='\n'.join(processed_list)
    return t
    

def oper(fct, s):
    if s and fct: 
        return fct(s)  # Apply the function to the string
    if s: 
        return rot(s)
    if fct: 
        return selfie_and_rot(s)  # Note: This might need to be fct instead of s, depending on your intent
    
    


if __name__ == '__main__':
    s= "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"
    fct="xZBV\njsbS\nJcpN\nfVnP"
    print(oper(fct,s)) 
   # oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"
   # oper(selfie_and_rot, s) => "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"