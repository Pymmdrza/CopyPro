
# all details can changed for needed 
# My contents on file txt's text this files ( add1trx , add2trx , add3trx , addTRX )

txtfiles = ['add1trx.txt','add2trx.txt','add3trx.txt','addTRX.txt']
with open ("MMDRZA.txt","w") as f:
    txt: str
    for txt in txtfiles:
        with open(txt) as f1:
            f.write(f1.read())
            f.write('\n')
