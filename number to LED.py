  
def Led(dig):
   output1=''
   output2=''
   output3=''
   output4=''
   output5=''

   for i2 in dig:
    i=int(i2)   
    s1='###   # ### ### # # ### ### ### ### ###'
    s2='# #   #   #   # # # #   #     # # # # #' 
    s3='# #   # ### ### ### ### ###   # ### ###' 
    s4='# #   # #     #   #   # # #   # # #   #' 
    s5='###   # ### ###   # ### ###   # ### ###'
    output1+=str(s1[i*4:i*4+4])
    output2+=str(s2[i*4:i*4+4])
    output3+=str(s3[i*4:i*4+4])
    output4+=str(s4[i*4:i*4+4])
    output5+=str(s5[i*4:i*4+4])
   output0=output1+'\n'+output2+'\n'+output3+'\n'+output4+'\n'+output5
   return output0
dig=input()
print(Led(dig))

