# Acha ab feature engineering hogai - tou ab kya karna hai: saaray kpis nikaalnay
# chalo dekhtay hain kpis kon konsay hain:
# appropriate opening (aik textual entailment ka model bana lo) - sai hai
# baaki tou bas word extraction ka aik feature banana hai for opening - for a call
# appropriate closing (Same - textual entailment ka model bana lo) - sai hai
# isska bhi bas aik feature add karna hai with suspected words for closing / goodbye
# issme abrupt call ending ya weird opening ka bhi check karna hai - okay?
# active listening - issme bhi textual entailment karni - baaki bas woi features nikalnay hongay - per sentence
# acha aur textual summarization ka model bhi banana hai - theek hai
# appropriate empathy - acha issme ab sentimental analysis aajata hai - bag of words model -
# hum har sentence kay words ko check kartay
# insult detector ka bhi aik feature ho jo bad words ko true karkay identify karde - jab nazar aae tou
# enthusiastic tone - issme hum bag of words model bana lete - plus aik feature
# joh words per minute frequency waghiara de de
# confidence and ownership - isskay leiy features chahiye aur phir textual entailment - so feature me yeh walay chahiye
# aik pronouns use, aik urmm, ermm, uhh walay parts of speech tags, aur hold ya transfer language
# easy understanding - word tokens ka fog index nikaloo
# noise ko use karo - aur customer kay samajh naa aanay walay sentences kay liey textual entailment
# phir call flow - yeh sab se mushkil hai, so filhaal miss scene
# appropriate probing - questions ka check lagao - aur phir find out kay questions sai hain
# issme bhi textual entailment hogi with dataset
# avoid excessive sir/ma'am - issme named entity recog for name and sir/maam
# coreference resolution bhi use hogi
# dead air check - hold times ka feature banao - isska koi threshold rakh lo
# customer verification - after opening, find verification questions - sai hai?
# named entity aur textual entailment use hoga
# speaker recognition - yeh bhi mushkil hoga - filhaal miss hai

