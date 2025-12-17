//  (* Code.4-M: AEAD_mac_then_enc_rogaway_scheme eufcma model with myoracle by python code*)
#!/usr/bin/python3

from __future__ import print_function
import sys

lines = sys.stdin.readlines()

la = []
lb = []
lc = []
ld = []
lemma = sys.argv[1]

for line in lines:
  num = line.split(':')[0]

  if lemma == "value_notequal":
      if ": St_ReceiveKey" in line:
        la.append(num)
      elif "(<enc(<~m, alicetag>, k2" in line or "(<enc(<~m, alicetag>, ~k2" in line:
        lb.append(num)
      elif "KU(key" in line or "KU(~key" in line:
        lc.append(num)
      else:
        ld.append(num)

  else:
    exit(0)

ranked = la + lb + lc + ld

for i in ranked:
  print(i)
