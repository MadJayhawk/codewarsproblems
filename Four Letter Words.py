''' 
5 kyu  Python
https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099

started: 5/29/24
completed: 7/2/24

'''

def find_word(word_list, wordx): 
    for word in word_list:
        if sum(a == b for a, b in zip(word, wordx)) == 3 and len(set(word))==len(word) and start!=word:
            return word
    return None

def mutations(alice, bob, word, first):
    global start
    l1=alice.copy()
    l2=bob.copy()
    start=word
    holdx=0
    while True:
        player=(l1,l2)[first]
        new_word=find_word(player,word)
        if new_word in l1:l1.remove(new_word) 
        if new_word in l2:l2.remove(new_word)
        if new_word:    
            holdx=1
            first=1-first 
            word=new_word 
        else:
            if holdx==1:
                return 1-first
            else:
                first=1-first
                player=(l1,l2)[first]
                new_word=find_word(player,word)
                if new_word:
                    return first
                else:
                    return -1