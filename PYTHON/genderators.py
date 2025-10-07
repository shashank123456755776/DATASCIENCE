# behave like a itertaors
# Generator = Function with yield.
# Used for large data, infinite data, memory efficiency.
# Works as an iterator.
# jab loops chnalna ho but we dont wants to use variables 
for _ in range(5):
    print("Hello")
#   return vs yield

# return → value देता है और function खत्म हो जाता है।

# yield → value देता है लेकिन function pause हो जाता है, अगली बार call करने पर वहीं से फिर continue होगा। 
# yield yaad rakhta hai jab hmm bare data ke sath kaam karte hai  
def number(n):
    while n>0:
        yield n
        n-=1
# Here generators in greating either by for loop and next()
for i in number(5):
    print(i)


# return क्या करता है?

# Value देता है

# Function पूरी तरह खत्म हो जाता है

# अगली बार call करने पर function फिर से शुरुआत से चलेगा

# 🔹 yield क्या करता है?

# Value देता है (जैसे return)

# लेकिन function खत्म नहीं होता, बस pause हो जाता है

# अगली बार जब generator को call करेंगे (next() या for loop), function pause वाली जगह से आगे continue होगा



# decorators and generators difference 
# decorators ka use hmm function mai extra functionality add karne ke liye karte hai with affect original function like authentication,two factor authentications 
# jaha genertaors ka use karte hai  bare data pe kaam karne mai such that pure iteratots pure memmory na le ekhi  value excute ho 



    