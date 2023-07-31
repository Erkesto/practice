#code shifts the alphabetic position by -2(or +24) that is g->e and so on
#found this code in python challenge.com
import string
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
          amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
          ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
          lmu ynnjw ml rfc spj."""
# method one 
table = string.maketrans( 
      string.ascii_lowercase , 
      string.ascii_lowercase[2:]+string.ascii_lowercase[:2] )
# method two 
# table = maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
#  text.translate (table)