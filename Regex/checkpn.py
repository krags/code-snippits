import re

def checkpn(cases):
    good=0
    bad=0
    # print(count)
    for pn in cases:
        x = re.match("(\d{4,7}_)(REV-)([A-Z]|\d|\d\d)[.](pdf|PDF)", pn)

        if x != None:
            print("Valid -> ", x.string)
            good += 1
        else:
            print("Not valid -> ", pn)
            bad+=1
    print('Valid qty = ', good)
    print('Not valid qty =', bad)
    
# Test cases
cases=[
'1234_REV-F.pdf',
'12345_REV-F.pdf',
'12346_REV-F.pdf',
'1234_REV-1.pdf',
'12345_REV-1.pdf',
'12346_REV-1.pdf',
'1234_REV-13.pdf',
'12345_REV-13.pdf',
'12346_REV-13.pdf',
'a123a3_REdddV-F.pdf',
'12345678_REV-F.pdf',
'123a567_REV-F.pdf',
'1234567-REV-F.pdf',
'1234567_rev-F.pdf',
'1234567_REV_F.pdf',
'1234567_REV-a.pdf',
'1234567_REV-123.pdf',
'1234567_REV-A1.pdf',
'1234567_REV-123.pdf',
'1234567_REV-1.PdF',
'1234567_REV-1.wrong'
]

checkpn(cases)
